#!/usr/bin/python3
from flask import Flask, request, Response, render_template, send_from_directory, jsonify
import queue
import configparser
import os
import json
from datetime import datetime
import cardmap
import punch_descriptions

app = Flask(__name__)
clients = []
_offsets = None
_punch_tooltip_grid = None
MAX_EAT_JSON_BYTES = 200_000
MAX_JSON_DEPTH = 10
MAX_JSON_CONTAINER_ITEMS = 5_000
MAX_JSON_STRING_LENGTH = 512
MAX_CARD_ROWS = 64
MAX_CARD_COLUMNS = 256
ALLOWED_EAT_JSON_KEYS = {'card', 'z_card', 'metadata'}

app.config['MAX_CONTENT_LENGTH'] = MAX_EAT_JSON_BYTES


def _validate_json_tree(value, depth=0):
    """Validate generic JSON to limit abusive nesting and oversized values."""
    if depth > MAX_JSON_DEPTH:
        return False, 'json too deeply nested'

    if isinstance(value, dict):
        if len(value) > MAX_JSON_CONTAINER_ITEMS:
            return False, 'json object too large'
        for key, item in value.items():
            if not isinstance(key, str):
                return False, 'json object keys must be strings'
            if len(key) > 128:
                return False, 'json object key too long'
            ok, reason = _validate_json_tree(item, depth + 1)
            if not ok:
                return ok, reason
        return True, None

    if isinstance(value, list):
        if len(value) > MAX_JSON_CONTAINER_ITEMS:
            return False, 'json array too large'
        for item in value:
            ok, reason = _validate_json_tree(item, depth + 1)
            if not ok:
                return ok, reason
        return True, None

    if isinstance(value, str):
        if len(value) > MAX_JSON_STRING_LENGTH:
            return False, 'json string value too long'
        return True, None

    if value is None or isinstance(value, (bool, int, float)):
        return True, None

    return False, 'unsupported json value type'


def _validate_card_matrix(card):
    """Validate expected punch card matrix shape and values."""
    if not isinstance(card, list) or not card:
        return False, 'card must be a non-empty array of rows'
    if len(card) > MAX_CARD_ROWS:
        return False, 'card has too many rows'

    width = None
    for row in card:
        if not isinstance(row, list) or not row:
            return False, 'each card row must be a non-empty array'
        if len(row) > MAX_CARD_COLUMNS:
            return False, 'card row has too many columns'
        if width is None:
            width = len(row)
        elif len(row) != width:
            return False, 'all card rows must have the same number of columns'

        for bit in row:
            if not isinstance(bit, bool):
                return False, 'card values must be booleans'

    return True, None


def get_offsets():
    global _offsets
    if _offsets is None:
        with open('cardpack/offsets.txt') as offsets:
            config = configparser.ConfigParser()
            config.read_string(offsets.read())
            _offsets = (
                float(config['Front']['originX']),
                float(config['Front']['originY']),
                float(config['Front']['offsetX']),
                float(config['Front']['offsetY']),
                int(config['Front']['t_start_x']),
                int(config['Front']['t_start_y'])
            )
    return _offsets


def _get_punch_tooltip_grid():
    """Return cached punch tooltip metadata for each card coordinate."""
    global _punch_tooltip_grid
    if _punch_tooltip_grid is None:
        rows = []
        for row in range(18):
            row_items = []
            for col in range(69):
                name = cardmap.punchName(row, col)
                description = None if name == '-' else punch_descriptions.PUNCH_DESCRIPTIONS.get(name)
                row_items.append({
                    'name': name,
                    'description': description,
                })
            rows.append(row_items)
        _punch_tooltip_grid = rows
    return _punch_tooltip_grid

def _list_saved_card_json_entries(limit=30):
    """Return newest saved card JSON entries with human-readable timestamps."""
    saved_json = [f for f in os.listdir('/tmp/cards/') if f.lower().endswith('_front.json')]
    saved_json.sort(key=lambda x: os.path.getmtime('/tmp/cards/' + x), reverse=True)
    entries = []
    for name in saved_json[:limit]:
        entries.append({
            "name": name,
            "date": _format_card_timestamp(name)
        })
    return entries

def _format_card_timestamp(filename):
    """Extract and format timestamp from card filename.
    
    Converts '26-03-22_21-32-16_front.json' to
    '2026-03-22 21:32:16'
    """
    try:
        # Extract the timestamp
        timestamp_part = os.path.basename(filename)[:17]  # '26-03-22_21-32-16'
        date_part, time_part = timestamp_part.split('_')
        yy, mm, dd = date_part.split('-')
        hh, minute, ss = time_part.split('-')
        
        # Convert YY to YYYY
        yyyy = f"20{yy}"
        
        # Format as YYYY-MM-DD HH:MM:SS
        return f"{yyyy}-{mm}-{dd} {hh}:{minute}:{ss}"
    except Exception:
        # Fallback to original filename if parsing fails
        return filename

def _get_bins():
    """Return a mapping of bin -> list of card data with filenames and formatted dates."""
    bins = {}
    for fn in os.listdir('/tmp/cards/'):
        if not fn.endswith('_front.json'):
            continue
        path = os.path.join('/tmp/cards', fn)
        try:
            with open(path) as f:
                data = json.load(f)
        except Exception:
            continue
        bin_name = data.get('metadata', {}).get('bin', 'unknown')
        json_name = fn[:-5] + '.json'
        formatted_date = _format_card_timestamp(json_name)
        register_digits = data.get('metadata', {}).get('register', {}).get('digits')
        if isinstance(register_digits, list):
            register_digits_display = ''.join(str(d) for d in register_digits)
        elif register_digits is None:
            register_digits_display = None
        else:
            register_digits_display = str(register_digits)
        bins.setdefault(bin_name, []).append({
            'filename': json_name,
            'date': formatted_date,
            'register_digits': register_digits,
            'register_digits_display': register_digits_display,
        })

    # Sort by filename (timestamp-prefixed), backwards
    for cards in bins.values():
        cards.sort(key=lambda x: x['filename'], reverse=True)

    return bins


@app.route('/eat_json', methods=['POST'])
# Accepts a JSON representation of a card (same format as ``cardpack/cardout_sample.json``)
def yumyum():
    if request.content_length is not None and request.content_length > MAX_EAT_JSON_BYTES:
        return jsonify({'error': 'payload too large'}), 413
    if not request.is_json:
        return jsonify({'error': 'content-type must be application/json'}), 415

    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({'error': 'request body must be a JSON object'}), 400

    unknown_keys = set(data.keys()) - ALLOWED_EAT_JSON_KEYS
    if unknown_keys:
        return jsonify({'error': 'unexpected top-level keys'}), 400

    card = data.get('card')
    if card is None:
        card = data.get('z_card')
    if card is None:
        return jsonify({'error': 'missing card data (card or z_card)'}), 400

    card_ok, card_reason = _validate_card_matrix(card)
    if not card_ok:
        return jsonify({'error': card_reason}), 400

    metadata = data.get('metadata')
    if metadata is not None and not isinstance(metadata, dict):
        return jsonify({'error': 'metadata must be an object'}), 400

    json_ok, json_reason = _validate_json_tree(data)
    if not json_ok:
        return jsonify({'error': json_reason}), 400

    now = datetime.now()
    punchdate = now.strftime('%y-%m-%d_%H-%M-%S-%f')
    os.makedirs("/tmp/cards", exist_ok=True)
    # this stores the entire card with metadata which is used for the bins page
    out_path = f'/tmp/cards/{punchdate}_front.json'
    with open(out_path, 'x') as f:
        json.dump(data, f, separators=(',', ':'))

    # scream at clients and tell them there's a new card
    for q in clients:
        q.put("update")

    return "Success", 200

@app.route('/events', methods=['GET'])
def events():
    """events endpoint for notifying clients of new cards"""
    def stream():
        q = queue.Queue()
        clients.append(q)
        # safari wants data immediately
        yield "data: connected\n\n"
        try:
            while True:
                msg = q.get()
                yield f"data: {msg}\n\n"
        except GeneratorExit:
            clients.remove(q)

    return Response(stream(), mimetype="text/event-stream")

@app.route('/credits', methods=['GET'])
def credits():
    """Serve the credits page."""
    return render_template('credits.html')

@app.route('/settings', methods=['GET'])
def settings():
    """Serve the settings page."""
    return render_template('settings.html')

@app.route('/blank-card', methods=['GET'])
def blank_card():
    """Serve the blank (unpunched) card template image."""
    return send_from_directory('cardpack', 'front_9a8sudf.jpg')

@app.route('/punch-tooltip-data', methods=['GET'])
def punch_tooltip_data():
    """Return static punch-name and description data for hover tooltips."""
    return jsonify(_get_punch_tooltip_grid())

@app.route('/latest-card-data', methods=['GET'])
def latest_card_data():
    """Return card bits + metadata for the most recently saved card."""
    entries = _list_saved_card_json_entries(limit=1)
    if not entries:
        return jsonify({"error": "no cards available"}), 404
    data = _load_card_metadata(entries[0]["name"])
    if data is None:
        return jsonify({"error": "metadata not found"}), 404
    return jsonify(data)

@app.route('/', methods=['GET'])
def display_cards():
    """# main page showing the most recent cards and allowing selection of past cards"""
    saved_cards = _list_saved_card_json_entries()
    orig_x, orig_y, off_x, off_y, _t_start_x, _t_start_y = get_offsets()
    return render_template("cards.html", card_entries=saved_cards,
                           orig_x=orig_x, orig_y=orig_y, off_x=off_x, off_y=off_y)

@app.route('/cardnames', methods=['GET'])
def get_cardnames():
    """Gets a JSON list of newest saved card metadata entries."""
    return jsonify(_list_saved_card_json_entries())

@app.route('/bins', methods=['GET'])
def view_bins():
    """Render an HTML report of all bins and their contents."""
    bins = _get_bins()
    return render_template('bins.html', bins=bins)

def _load_card_metadata(name):
    """Load saved card JSON (card + metadata) by JPG name, JSON name, or base."""
    if name.lower().endswith('.json'):
        base = os.path.splitext(name)[0]
    else:
        base = name
    meta_path = os.path.join('/tmp/cards', f"{base}.json")
    if not os.path.exists(meta_path):
        return None
    with open(meta_path) as f:
        return json.load(f)

@app.route('/cardmeta/<name>', methods=['GET'])
def card_metadata(name):
    """Return saved evaluation metadata for a card."""
    data = _load_card_metadata(name)
    if data is None:
        return jsonify({"error": "metadata not found"}), 404
    return jsonify(data)

@app.route('/card/<name>', methods=['GET'])
def single_card(name):
    """Render a card view page, drawing the card from stored JSON data."""
    data = _load_card_metadata(name)
    orig_x, orig_y, off_x, off_y, _t_start_x, _t_start_y = get_offsets()

    # Determine prev/next card by time (filename sort order)
    base = os.path.splitext(name)[0]
    json_name = f"{base}.json" if not base.endswith('_front') else f"{base}.json"
    all_cards = sorted(f for f in os.listdir('/tmp/cards/') if f.endswith('_front.json'))
    prev_card = next_card = None
    if json_name in all_cards:
        idx = all_cards.index(json_name)
        prev_card = all_cards[idx - 1] if idx > 0 else None
        next_card = all_cards[idx + 1] if idx < len(all_cards) - 1 else None

    pretty_json = None if data is None else json.dumps(data, indent=2, sort_keys=True)

    if data is None:
        return render_template('card_view.html', card_name=name,
                               card_data_json='null',
                               pretty_json=pretty_json,
                               prev_card=prev_card, next_card=next_card,
                               orig_x=orig_x, orig_y=orig_y,
                               off_x=off_x, off_y=off_y), 404
    return render_template('card_view.html', card_name=name,
                           card_data_json=json.dumps(data),
                           pretty_json=pretty_json,
                           prev_card=prev_card, next_card=next_card,
                           orig_x=orig_x, orig_y=orig_y,
                           off_x=off_x, off_y=off_y)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5220)