#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
from PIL import Image

from screen.log import Logger

# Get logger
logger = Logger()

# Get the path to the project
top_level = os.path.dirname(os.path.abspath(os.path.dirname(__file__))).split('/screen')[0]
config_path = os.path.join(top_level, 'config')
render_path = os.path.join(top_level, 'render')
