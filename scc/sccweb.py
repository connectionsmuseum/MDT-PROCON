#!/usr/bin/python3
from flask import Flask, request, render_template
from flask_api import status
import math
import sys
import zipfile
from PIL import Image, ImageDraw
import configparser
import os
import json
import random
from twython import Twython
import io
from datetime import datetime
import pprint   #XXX sarah
from mastodon import Mastodon


app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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


# (bw0 .. bw59) -> R section
# (bw60 .. bw119) -> S section


with open('5xb-tweets.txt') as x:
    exclamations = x.readlines()

def deep_scan_to_namescan(scan):
    out = {}
    for i in range(16):
        for j in range(10):
            out[scanpts_order[i][j]] = scan["%d"%i][j]
    return out

def unfold_scans(dump):
    namescan = {k: deep_scan_to_namescan(v) for k, v in dump.items()}
    return namescan

@app.route('/punch', methods=['POST'])
def req_punch():
    dump = request.get_json()
    leads = unfold_scans(dump)
    card = operate(leads)

    # make card images
    print(print_card(card))
    punch_card(card)

    # save card info
    save_card(card)
    return "", status.HTTP_200_OK

def scan_data_to_card(data):
    card = [[False for x in range(69)] for y in range(18)]

    for scan_group in range(9):
        for i in range(16):
            for j in range(8):
                row = 8 - scan_group
                scanpt_val = scanpts_order[i][j]
                if isinstance(scanpt_val, int):
                    col = scanpt_val % 30
                    if 0 <= scanpt_val and scanpt_val <= 29:
                        row += 9
                    if 30 <= scanpt_val and scanpt_val <= 59:
                        row += 9
                        col += 39
                    if 60 <= scanpt_val and scanpt_val <= 89:
                        pass
                    if 90 <= scanpt_val and scanpt_val <= 119:
                        col += 39
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
                        # app.logger.debug(f"on iteration s{scan_group} i{i} j{j} got row{row} col{col}")
                        card[row][col] = True
    return card

@app.route('/trouble-card', methods=['POST'])
def req_trouble_card():
    if request.content_length < 2**16:
        data = request.get_data(as_text=True)
        # app.logger.debug(f"received '{data}'")
        split_data = data.split(',')
        decoded_data = list(map(lambda x: int(x, 16), split_data))
        # app.logger.debug(f"decoded {decoded_data}")
        card = scan_data_to_card(decoded_data)
        print(print_card(card))
        #app.logger.debug(md5(data.encode()).hexdigest())

        punch_card(card)
        save_card(card)

        return {}

def reorder_dict(dump):
    reordered_data = {}
    for outer_key, inner_dict in dump.items():
        sorted_keys = sorted(inner_dict.keys(), key=lambda x: (x != '0', x == '15', int(x)))
        reordered_data[outer_key] = {k: inner_dict[k] for k in sorted_keys}
    return reordered_data

def save_card(card):
    name = "/tmp/cardout-date.json"
    with open(name, "w") as f:
        json.dump(card, f)

def print_card(card):
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

def punch_card(bits):
    now = datetime.now()
    punchdate = now.strftime("%y-%m-%d_%H-%M")

    with zipfile.ZipFile('cardpack.zip') as cardpack:
        f_im=Image.open(cardpack.open('front.png'))
        #b_im=Image.open(cardpack.open('back.png'))
        with cardpack.open('offsets.txt') as offsets:
            config=configparser.ConfigParser()
            config.read_string(offsets.read().decode('ASCII'))
            f_origin_x=float(config['Front']['originX'])
            f_origin_y=float(config['Front']['originY'])
            f_offset_x=float(config['Front']['offsetX'])
            f_offset_y=float(config['Front']['offsetY'])
            b_origin_x=float(config['Back' ]['originX'])
            b_origin_y=float(config['Back' ]['originY'])
            b_offset_x=float(config['Back' ]['offsetX'])
            b_offset_y=float(config['Back' ]['offsetY'])

        holesize = 15
        #Render the PNGs
        f_draw = ImageDraw.Draw(f_im)
        #b_draw = ImageDraw.Draw(b_im)
        for xidx in range(69):
            for yidx in range(18):
                if xidx>30 and xidx<38: continue
                #Don't tell Professor Mead, these numbers are magic
                f_xcen=f_origin_x+(xidx*f_offset_x)
                f_ycen=f_origin_y+(yidx*f_offset_y)
                b_xcen=b_origin_x+(xidx*b_offset_x)
                b_ycen=b_origin_y+(yidx*b_offset_y)
                #It's hole-punchin' time
                if bits[yidx][xidx]:
                    f_draw.ellipse([(f_xcen - holesize, f_ycen - holesize),
                                    (f_xcen + holesize, f_ycen + holesize)],
                                   'black', 'black')
                   # b_draw.ellipse([(b_xcen - holesize, b_ycen - holesize),
                   #                 (b_xcen + holesize, b_ycen + holesize)],
                   #                'black', 'black')
        # save the cards to be used via the web frontend
        rgb_im  = f_im.convert('RGB')
        rgb_im.save("/tmp/front.jpg", optimize=True)
        #b_im.save("/tmp/back.png", format="PNG", optimize=True)

        # and save the cards to a directory so I can look at them later
        f_im.save("/tmp/cards/" + punchdate + "front.png", format="PNG", optimize=True)
        #b_im.save("/tmp/cards/" + punchdate + "back.png", format="PNG", optimize=True)


def operate(leads):
    card = [[False for x in range(69)] for y in range(18)]
    for S in range(9):
        Sx = "S{}".format(S)    # each scanning relay 0-8
        for k in leads[Sx]:     # going into the nest "k"
            row = 8-S           # S0 for example will give row = 8
            if isinstance(k, int):
                column = k%30
                if k>=0 and k<=29:
                    # 0 to 29, bottom left 'R'
                    row += 9

                if k>=30 and k<=59:
                    # 30 to 59, bottom right 'RA'
                    row += 9
                    column += 39

                if k>=60 and k<=89:
                    # 60 to 89, top left 'S'
                    True

                if k>=90 and k<=119:
                    # 90 to 119, top right 'SA'
                    column += 39

            elif k == "BWX0":
                # after 29, so bottom left
                column = 30
                row += 9

            elif k == "BWX1":
                # before 30, so bottom right
                column = 38
                row += 9

            elif k == "BWX2":
                # after 89
                column = 30

            elif k == "BWX3":
                # before 90
                column = 38

            if ((leads[Sx][k] == 1) and (column is not None) and isinstance(k, int)):
                card[row][column] = True
    return card

@app.route('/punch', methods=['GET'])
def displaycard():
    return render_template("index.html", front="static/front.jpg")

@app.route('/mastodon', methods=['POST'])
def button_click():
    # make card text
    # cardtext = print_card(card)
    flavor = random.choice(exclamations)
    # print(cardtext)
    print(flavor)
    with open('/etc/sccweb.conf') as secrets:
        config = configparser.ConfigParser()
        config.read_string(secrets.read())

        ffront = open("/tmp/front.jpg", 'rb')
        #fback = open("/tmp/back.png", 'rb')

    return render_template("index.html", front="static/front.jpg")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5220)

