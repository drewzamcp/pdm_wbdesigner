#! user/env/python
import sys
from pathlib import Path

from pdm_project_one.library import imgtools


def create_artwork(text_input: str, input_img_url: Path):  # sourcery skip: inline-immediately-returned-variable
    # text_input = input("Enter text for wristband: ")
    # img_url_input = input("Enter path to image: ")

    if not Path(input_img_url).exists():
        print(f"Cannot find file path: {input_img_url}")
        sys.exit(1)

    transparent_img = wristband_image(
        input_img_url,
        text_input,
    )

    print(f"{transparent_img} created")
    return transparent_img


def wristband_image(img_path, input_text: str):
    """
    Starting point for most artworks. Handles the conversion of different
    image versions (*.png, *.jpg, *.pdf)
    """
    # upload image in supported format (*.png, *.jpg, *.pdf)
    # convert the image to black and white bitmap
    # remove background
    transparent_image = imgtools.get_transparent_image(img_path)
    # resize to fit wristband

    return imgtools.add_text_image(transparent_image, input_text)


