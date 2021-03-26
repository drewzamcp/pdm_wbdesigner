#! user/env/python
from PIL import Image, ImageOps
from pdm_project_one import image_tools

MAX_HEIGHT = 72  # measured in pixels


def main():  # sourcery skip: inline-immediately-returned-variable
    transparent_img = wristband_image(
        "/Users/drewmac/webdev/pdm-project1/image_folder/raw/Northern Farm.jpg"
    )
    return transparent_img


def wristband_image(img_path):
    """
    Starting point for most artworks. Handles the conversion of different
    image versions (*.png, *.jpg, *.pdf)
    """
    # upload image in supported format (*.png, *.jpg, *.pdf)
    # convert the image to black and white bitmap
    # remove background
    transparent_image = image_tools.get_transparent_image(img_path)
    # resize to fit wristand

    return transparent_image


if __name__ == "__main__":
    main()
