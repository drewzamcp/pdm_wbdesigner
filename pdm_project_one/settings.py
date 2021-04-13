#!/usr/bin/env python
from decouple import config

# Settings
IMG_INPUT_FLDR = config("IMG_INPUT_FLDR")
IMG_OUTPUT_FLDR = config("IMG_OUTPUT_FLDR")

# Fonts
FONT_FOLDER = config("FONT_FOLDER")

# FastAPI
TEMPLATE_FLDR = config("TEMPLATE_FLDR")
