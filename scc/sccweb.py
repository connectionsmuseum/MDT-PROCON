#!/usr/bin/python3
from flask import Flask, request
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

app = Flask(__name__)

scanpts_order = [
     7,  6,  5,  4,  3,  2,  1,  0, 'STRA1', 'STR',
    15, 14, 13, 12, 11, 10,  9,  8, 'TRC', 'SPL',
    23, 22, 21, 20, 19, 18, 17, 16, 'ROS', 'MB',
    'BWX1', 'BWX0', 29, 28, 27, 26, 25, 24, 'RSV3.8', 'RSV3.9',
    37, 36, 35, 34, 33, 32, 31, 30, 'RSV4.8', 'RSV4.9',
    45, 44, 43, 42, 41, 40, 39, 38, 'RSV5.8', 'RSV5.9',
    53, 52, 51, 50, 49, 48, 47, 46, 'RSV6.8', 'RSV6.9',
    61, 60, 59, 58, 57, 56, 55, 54, 'RSV7.8', 'RSV7.9',
    69, 68, 67, 66, 65, 64, 63, 62, 'RSV8.8', 'RSV8.9',
    77, 76, 75, 74, 73, 72, 71, 70, 'RSV9.8', 'RSV9.9',
    85, 84, 83, 82, 81, 80, 79, 78, 'RSV10.8', 'RSV10.9',
    91, 90, 'BWX3', 'BWX2', 89, 88, 87, 86, 'RSV11.8', 'RSV11.9',
    99, 98, 97, 96, 95, 94, 93, 92, 'RSV12.8', 'RSV12.9',
    107, 106, 105, 104, 103, 102, 101, 100, 'RSV13.8', 'RSV13.9',
    115, 114, 113, 112, 111, 110, 109, 108, 'RSV14.8', 'RSV14.9',
    'RSV15.0', 'RSV15.1', 'RSV15.2', 'RSV15.3', 119, 118, 117, 116, 'RSV15.8', 'RSV15.9'
    ]

with open('/opt/MDT-PROCON/scc/5xb-tweets.txt') as x:
    exclamations = x.readlines()

def deep_scan_to_namescan(scan):
    out = {}
    for i in range(len(scanpts_order)-1):
        j = int(i)%16
        k = math.floor(int(i)/16)
        out[scanpts_order[i]] = scan[j][k]
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
    punch_card(card)
    # save card info
    save_card(card)
    # put on twitter
    post_card(card)
    return "", status.HTTP_200_OK

def save_card(card):
    name = "/tmp/cardout-date.json"
    with open(name, "w") as f:
        json.dump(card, f)

def post_card(card):
    # make card text
    cardtext = print_card(card)
    flavor = random.choice(exclamations)
    print(cardtext)
    print(flavor)
    with open('secrets.ini') as secrets:
        config = configparser.ConfigParser()
        config.read_string(secrets.read())
        twitter = Twython(
            app_key = config['secrets']['api_key'],
            app_secret = config['secrets']['api_secret'],
            oauth_token = config['fivecrossbar']['access_token'],
            oauth_token_secret = config['fivecrossbar']['access_secret'],)
        ffront = open("/tmp/front.png", 'rb')
        fback = open("/tmp/back.png", 'rb')
        front_resp = twitter.upload_media(media=ffront)
        back_resp = twitter.upload_media(media=fback)
        resp = twitter.update_status(status=flavor, 
                              media_ids=[
                                  front_resp['media_id']
                                  ,back_resp['media_id']
                              ]
        )
        return resp['id']

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
    with zipfile.ZipFile('cardpack.zip') as cardpack:
        f_im=Image.open(cardpack.open('front.png'))
        b_im=Image.open(cardpack.open('back.png'))
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
        b_draw = ImageDraw.Draw(b_im)
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
                    b_draw.ellipse([(b_xcen - holesize, b_ycen - holesize),
                                    (b_xcen + holesize, b_ycen + holesize)],
                                   'black', 'black')
        f_im.save("/tmp/front.png", format="PNG", optimize=True)
        b_im.save("/tmp/back.png", format="PNG", optimize=True)


def operate(leads):
    card = [[False for x in range(69)] for y in range(18)]
    for S in range(9):
        Sx = "S{}".format(S)
        for k in leads[Sx]:
            row = S
            if isinstance(k, int):
                zone = math.floor(k/30)
                column = k%30
                if zone==0:
                    # top left
                    row = row
                if zone==1:
                    # top right
                    column += 39
                if zone==2:
                    # bottom left
                    row += 9
                if zone==3:
                    # bottom right
                    row += 9
                    column += 39
            elif k == "BWX0":
                column = 30
            elif k == "BWX1":
                column = 30
                row += 9
            elif k == "BWX2":
                column = 38
            elif k == "BWX3":
                column = 38
                row += 9
            if ((leads[Sx][k] == 1) and (column is not None)):
                card[row][column] = True
    return card

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5220)
