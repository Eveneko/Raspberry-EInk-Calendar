#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from log import log

render_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'render')


class RenderHelper:

    def __init__(self, width, height, routate_angle, html_file, html_template):
        self.width = width
        self.height = height
        self.routate_angle = routate_angle
        self.html_file = html_file
        self.html_template = html_template
        self.logger = log.Logger()
    
    def set_viewport_size(self, driver):

        # Extract the current window size from the driver
        current_window_size = driver.get_window_size()

        # Extract the client window size from the html tag
        html = driver.find_element_by_tag_name('html')
        inner_width = int(html.get_attribute("clientWidth"))
        inner_height = int(html.get_attribute("clientHeight"))

        # "Internal width you want to set+Set "outer frame width" to window size
        target_width = self.width + (current_window_size["width"] - inner_width)
        target_height = self.height + (current_window_size["height"] - inner_height)

        driver.set_window_rect(
            width=target_width,
            height=target_height)
        
    def get_screenshot(self):
        opts = Options()
        opts.add_argument("--headless")
        opts.add_argument('--no-sandbox')
        opts.add_argument("--hide-scrollbars");
        opts.add_argument('--force-device-scale-factor=1')
        driver = webdriver.Chrome(options=opts)
        driver.get(self.html_file)
        sleep(1)
        img_path = os.path.join(render_dir, self.html_file.split('.')[0]+'.png')
        driver.get_screenshot_as_file(img_path)
        driver.quit()

        self.logger.info('Screenshot captured and saved to file.')

        black_image = Image.open(img_path)
        black_pixels = black_image.load()
        red_image = Image.open(img_path)
        red_pixels = black_image.load()

        for i in range(red_image.size[0]):
            for j in range(red_image.size[1]):
                if red_pixels[i, j][0] <= red_pixels[i, j][1] and red_pixels[i, j][0] <= red_pixels[i, j][2]:  # if is not red
                    red_pixels[i, j] = (255, 255, 255)  # change it to white in the red image bitmap

                elif black_pixels[i, j][0] > black_pixels[i, j][1] and black_pixels[i, j][0] > black_pixels[i, j][2]:  # if is red
                    black_pixels[i, j] = (255, 255, 255)  # change to white in the black image bitmap

        red_image = red_image.rotate(self.rotate_angle, expand=True)
        black_image = black_image.rotate(self.rotate_angle, expand=True)

        self.logger.info('Image colours processed. Extracted grayscale and red images.')
        return black_image, red_image
        