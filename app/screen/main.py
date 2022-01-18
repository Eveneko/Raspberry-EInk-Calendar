#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from log.logger import Logger


def main():
    # Basic configuration settings
    config_file = open('config/config.json')
    config = json.load(config_file)

    # Create logger
    logger = Logger('INFO')


if __name__ == "__main__":
    main()
