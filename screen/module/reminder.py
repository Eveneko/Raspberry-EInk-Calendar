#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from log import log
from display.display import DisplayHelper
from render.render import RenderHelper

config_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config')
render_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'render')


def process(render: RenderHelper):
    html_file_path = os.path.join(render_dir, render.html_file)
    html_template_path = os.path.join(render_dir, render.html_template)
    with open(html_template_path, 'r') as f:
        template = f.read()
    with open(html_file_path, 'w') as f:
        f.write(template)
    
    return render.get_screenshot()


def main():
    # Basic configuration setting
    config_file_path = os.path.join(config_dir, 'reminder.json')
    with open(config_file_path, 'r') as f:
        config = json.load(f)

    width = config['width']
    height = config['height']
    routate_angle = config['routate_angle']
    html_file = config['html_file']
    html_template = config['html_template']

    # Load logger
    logger = log.Logger()

    # Process html
    display_service = DisplayHelper(width, height)
    render_service = RenderHelper(width, height, routate_angle, html_file, html_template)

    black_image, red_image = process(render_service)
    display_service.update(black_image, red_image)
    display_service.sleep()


if __name__ == "__main__":
    main()
