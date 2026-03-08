#!/usr/bin/python3
from flask import Flask, request, Response, render_template, send_from_directory, redirect, jsonify
import queue
from PIL import Image, ImageDraw
import configparser
import os
import json
from datetime import datetime

app = Flask(__name__)
clients = []
_offsets = None

# The virtual card is scanned in 120 points (two rows) at a time, in the same
# way as the actual card is punched when it is transported through the trouble recorder.
# (bw0 .. bw59) -> R, RA section
# (bw60 .. bw119) -> S, SA section
# The following list gives the order of the scan points for the two rows of each scan as we get
# them from the MDT.
# The final card will contain this list 9 times, once for each of the 9 punch cycles (S0 to S8).
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
    6: [2,4],
    7: [0,4],
    8: [1,4],
    9: [2,4]
}

def convert_to_card(data):
# Convert scan data into a 2D card representation.

    card = [[False for x in range(69)] for y in range(18)]

    for scan_group in range(9):
        for i in range(16):
            for j in range(8):
                row = 8 - scan_group
                scanpt_val = scanpts_order[i][j]
                if isinstance(scanpt_val, int):
                    col = scanpt_val % 30
                    if 0 <= scanpt_val and scanpt_val <= 29:
                        # bottom left 'R'
                        row += 9
                    if 30 <= scanpt_val and scanpt_val <= 59:
                        # bottom right 'RA'
                        row += 9
                        col += 39
                    if 60 <= scanpt_val and scanpt_val <= 89:
                        # top left 'S'
                        pass
                    if 90 <= scanpt_val and scanpt_val <= 119:
                        # top right 'SA'
                        col += 39
                # Note: these are never written, regardless of value, due to the isinstance check below
                elif scanpt_val == 'BWX0':
                    col = 30
                    row += 9
                elif scanpt_val == 'BWX1':
                    col = 38
                    row += 9
                elif scanpt_val == 'BWX2':
                    col = 30
                elif scanpt_val == 'BWX3':
                    col = 38

                if (((data[scan_group * 16 + i] >> j) & 1) == 1) and isinstance(scanpt_val, int):
                    if row < 18 and col < 69:
                        card[row][col] = True
    return card

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

def punch_card(bits):
# creates a card image complete with holes punched in the right places,
# and saves it to disk with a timestamped filename
    orig_x, orig_y, off_x, off_y, t_start_x, t_start_y = get_offsets()
    f_im=Image.open('cardpack/front.jpg')

    holesize = 15
    now = datetime.now()
    punchdate = now.strftime("%y-%m-%d_%H-%M-%S")

    time_dict = {
        'day_tens': int(now.strftime("%d")) // 10,
        'day_units': int(now.strftime("%d")) % 10,
        'hour_tens': int(now.strftime("%H")) // 10,
        'hour_units': int(now.strftime("%H")) % 10,
        'minute_tens': int(now.strftime("%M")) // 10,
        'minute_units': int(now.strftime("%M")) % 10
    }

    for key, value in time_dict.items():
        holes = two_of_five[value]
        for hole in holes:
            # print(f"Punching hole for {key} in position {hole}")
            bits[t_start_y][t_start_x + hole] = True
        t_start_x += 5

        #Render the JPG
        f_draw = ImageDraw.Draw(f_im)
        for xidx in range(69):
            for yidx in range(18):
                if xidx>30 and xidx<38: continue
                #Don't tell Professor Mead, these numbers are magic
                f_xcen=orig_x+(xidx*off_x)
                f_ycen=orig_y+(yidx*off_y)

                #It's hole-punchin' time! KACHUKACHUKACHUKA
                if bits[yidx][xidx]:
                    f_draw.ellipse([(f_xcen - holesize, f_ycen - holesize),
                                    (f_xcen + holesize, f_ycen + holesize)],
                                   'black', 'black')

        # save the cards to be used via the web frontend
        f_im.save("/tmp/front.jpg", optimize=True)

        # and save the cards to a directory so I can look at them later
        f_im.save("/tmp/cards/" + punchdate + "_front.jpg", optimize=True)

def ascii_card(card):
# mostly not used in production. provides a text representation of the card in the terminal
    text = ''
    text += ('+'+('—'*69)+'+\n')
    for y in range(18):
        text += ('|')
        for x in range(69): #nice
            if x==31 or x==37:
                text += ('|')
            elif x>31 and x<37:
                text += (' ')
            else:
                text += ('#' if card[y][x] else '·')
        text += ('|\n')
    text += ('+'+('—'*69)+'+\n')
    return text

def save_json_to_disk(card):
    name = "/tmp/cardout_most_recent.json"
    with open(name, "w") as f:
        json.dump(card, f)


@app.route('/trouble-card', methods=['POST'])
# MDT posts cards here
def receive_trouble_card():
    if request.content_length < 2**16:
        data = request.get_data(as_text=True)
        split_data = data.split(',')
        decoded_data = list(map(lambda x: int(x, 16), split_data))
        card = convert_to_card(decoded_data)
        punch_card(card)
        print(ascii_card(card))
        save_json_to_disk(card)

        # notify any connected clients that a new card is available
        for q in clients:
            q.put("update")

        return {}, 200

@app.route('/test', methods=['POST'])
# test endpoint for manually triggering an update event to connected
# clients without needing to send a card from the MDT
def test():
    data = [[False for x in range(69)] for y in range(18)]
    punch_card(data)

    for q in clients:
        q.put("update")
    return {}, 200

@app.route('/events', methods=['GET'])
# events endpoint for notifying clients of new cards
def events():
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

@app.route('/', methods=['GET'])
# main page showing the most recent cards and allowing selection of past cards
def display_cards():
    saved_cards = os.listdir('/tmp/cards/')
    saved_cards.sort(key=lambda x: os.path.getmtime('/tmp/cards/' + x))
    saved_cards = saved_cards[::-1]
    saved_cards = saved_cards[:30]
    return render_template("cards.html", cardnames=saved_cards)

@app.route('/cardnames', methods=['GET'])
# gets the list of saved cards
def get_cardnames():
    saved_cards = os.listdir('/tmp/cards/')
    saved_cards.sort(key=lambda x: os.path.getmtime('/tmp/cards/' + x))
    saved_cards = saved_cards[::-1]
    saved_cards = saved_cards[:30]
    return jsonify(saved_cards)

@app.route('/cards', methods=['GET'])
# for backward compatibility with older versions of the frontend
def go_away():
    return redirect('/', code=301)

@app.route('/card/<name>', methods=['GET'])
# used by the frontend to request a specific card from a dropdown
def single_card(name):
    return send_from_directory('/tmp/cards', name)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5220)