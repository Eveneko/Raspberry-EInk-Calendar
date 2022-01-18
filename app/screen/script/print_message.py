#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
display_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'display')
if os.path.exists(display_dir):
    sys.path.append(display_dir)

import logging
# from ..display import epd7in5b_V2
import epd7in5b_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)


def print_message(message):
    try:
        epd = epd7in5b_V2.EPD()
        logging.info("init and Clear")
        epd.init()
        epd.Clear()

        font48 = ImageFont.truetype(os.path.join(display_dir, 'Font.ttc'), 48)
        font24 = ImageFont.truetype(os.path.join(display_dir, 'Font.ttc'), 24)
        font18 = ImageFont.truetype(os.path.join(display_dir, 'Font.ttc'), 18)

        Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
        Other = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
        draw_Himage = ImageDraw.Draw(Himage)
        draw_other = ImageDraw.Draw(Other)
        draw_Himage.text((300, 0), message, font = font48, fill = 0)
        epd.display(epd.getbuffer(Himage),epd.getbuffer(Other))

    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd7in5b_V2.epdconfig.module_exit()
        exit()
