#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from importlib import import_module

from screen.custom import *


class Display:

    def __init__(self, driver_name):
        self.driver_name = driver_name
        self.get_driver()
        self.get_display_size()

    def get_driver(self):
        try:
            driver_path = f'screen.display.driver.{self.driver_name}'
            self.driver = import_module(driver_path)
            self.epd = self.driver.EPD()

        except ImportError:
            raise Exception('This module is not supported. Check your spellings?')

        except FileNotFoundError:
            raise Exception('SPI could not be found. Please check if SPI is enabled')
    
    def get_display_size(self):
        self.width = self.driver.EPD_WIDTH
        self.height = self.driver.EPD_HEIGHT

    def update(self, black_image, red_image):
        self.epd.clear()
        self.epd.display(black_image, red_image)
        logger.info(f'Screen display update complete')

    def sleep(self):
        self.epd.sleep()
        logger.info(f'Screen display sleep')

    def calibrate(self, cycles=1):
        self.epd.init()
        white = Image.new('1', (self.width, self.height), 'white')
        black = Image.new('1', (self.width, self.height), 'black')
        for _ in range(cycles):
            self.epd.display(black, white)
            self.epd.display(white, black)
            self.epd.display(white, white)
        logger.info(f'Screen display calibrate complete')
