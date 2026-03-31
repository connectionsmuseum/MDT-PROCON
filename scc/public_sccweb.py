#!/usr/bin/python3
from flask import Flask, request, Response, render_template, send_from_directory, redirect, jsonify
import queue
from PIL import Image, ImageDraw
import configparser
import os
import json
import cardmap as cm
import evaluatecard as ec
from datetime import datetime

app = Flask(__name__)
clients = []
_offsets = None

# The virtual card is scanned in 120 points (two rows) at a time, in the same
# way as the actual card is punched when it is transported through the trouble 
# recorder.
# (bw0 .. bw59) -> R, RA section
# (bw60 .. bw119) -> S, SA section
# The following list gives the order of the scan points for the two rows of 
# each scan as we get them from the MDT.
# The final card will contain this list 9 times, once for each of the 9 punch cycles (S0 to S8).
# The 'STR', 'SPL', 'RSVx.y', entries do not actually exist on the card, but
# are used by the MDT for its own internal functions.
scanpts_order = [
    [ 7,  6,  5,  4,  3,  2,  1,  0, 'STRA1', 'STR'],
    [15, 14, 13, 12, 11, 10,  9,  8, 'TRC', 'SPL'],
    [23, 22, 21, 20, 19, 18, 17, 16, 'ROS', 'MB'],
    ['BWX1', 'BWX0', 29, 28, 27, 26, 25, 24, 'RSV3.8', 'RSV3.9'],
    [37, 36, 35, 34, 33, 32, 31, 30, 'RSV4.8', 'RSV4.9'],
    [45, 44, 43, 42, 41, 40, 39, 38, 'RSV5.8', 'RSV5.9'],
    [53, 52, 51, 50, 49, 48, 47, 46, 'RSV6.8', 'RSV6.9'],
    [61, 60, 59, 58, 57, 56, 55, 54, 'RSV7.8', 'RSV7.9'],
    [69, 68, 67, 66, 65, 64, 63, 62, 'RSV8.8', 'RSV8.9'],
    [77, 76, 75, 74, 73, 72, 71, 70, 'RSV9.8', 'RSV9.9'],
    [85, 84, 83, 82, 81, 80, 79, 78, 'RSV10.8', 'RSV10.9'],
    [91, 90, 'BWX3', 'BWX2', 89, 88, 87, 86, 'RSV11.8', 'RSV11.9'],
    [99, 98, 97, 96, 95, 94, 93, 92, 'RSV12.8', 'RSV12.9'],
    [107, 106, 105, 104, 103, 102, 101, 100, 'RSV13.8', 'RSV13.9'],
    [115, 114, 113, 112, 111, 110, 109, 108, 'RSV14.8', 'RSV14.9'],
    ['RSV15.0', 'RSV15.1', 'RSV15.2', 'RSV15.3', 119, 118, 117, 116, 'RSV15.8', 'RSV15.9']
]

# helpful dictionary for punching the timestamp in the correct two-of-five holes on the card
two_of_five = {
    0: [3,4],
    1: [0,1],
    2: [0,2],
    3: [1,2],
    4: [0,3],
    5: [1,3],
    6: [2,3],
    7: [0,4],
    8: [1,4],
    9: [2,4]
}

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
    
    Converts '26-03-22_21-32-16_front.jpg' or '_front.json' to
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
        jpg_name = fn[:-5] + '.jpg'
        formatted_date = _format_card_timestamp(jpg_name)
        register_digits = data.get('metadata', {}).get('register', {}).get('digits')
        if isinstance(register_digits, list):
            register_digits_display = ''.join(str(d) for d in register_digits)
        elif register_digits is None:
            register_digits_display = None
        else:
            register_digits_display = str(register_digits)
        bins.setdefault(bin_name, []).append({
            'filename': jpg_name,
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
    card = None
    # first, try to parse the body as JSON
    if request.is_json:
        data = request.get_json() # this is the full card with metadata
        try:
            card = data["card"] # extracts just the holes
        except Exception:
            card = data["z_card"] # extracts just the holes
    else:
        # fallback: try reading raw data and parsing
        try:
            card = json.loads(request.get_data(as_text=True))
        except Exception:
            pass

    if card is None:
        return {"error": "no card data provided"}, 400

    now = datetime.now()
    punchdate = now.strftime("%y-%m-%d_%H-%M-%S")
    os.makedirs("/tmp/cards", exist_ok=True)
    # this stores the entire card with metadata which is used for the bins page
    with open(f"/tmp/cards/{punchdate}_front.json", "w") as f:
        json.dump(data, f)

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

@app.route('/blank-card', methods=['GET'])
def blank_card():
    """Serve the blank (unpunched) card template image."""
    return send_from_directory('cardpack', 'front.jpg')

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
    elif name.lower().endswith('.jpg'):
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
    """Return saved evaluation metadata for a card JPG."""
    data = _load_card_metadata(name)
    if data is None:
        return jsonify({"error": "metadata not found"}), 404
    return jsonify(data)

@app.route('/cards', methods=['GET'])
# for backward compatibility with older versions of the frontend
def go_away():
    return redirect('/', code=301)

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