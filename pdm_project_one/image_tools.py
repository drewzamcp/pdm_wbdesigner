#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import datetime as dt

COLOR_THRESHOLD = 180
FILE_DATE = dt.datetime.now().isoformat("-", "auto")
MAX_HEIGHT = 72
MAX_WIDTH = 720


def get_transparent_image(imagefile):

    img = Image.open(imagefile)
    rgba = img.convert("RGBA")
    datas = rgba.getdata()

    new_data = []
    for item in datas:
        if all(item > COLOR_THRESHOLD for item in item[:3]):
            row = (255, 255, 255, 0)
        else:
            row = (0, 0, 0, 255)
        new_data.append(row)

    output_path = "/Users/drewmac/webdev/pdm-project1/image_folder/processed/"
    outfile_name = f"processed_{FILE_DATE}_transparent.png"

    rgba.putdata(new_data)
    rgba.save(f"{output_path}{outfile_name}", "PNG")

    return rgba


def add_text_image(image: Image, text: str):

    base_layer = Image.new("RGBA", (MAX_HEIGHT, MAX_WIDTH), (255, 255, 255, 0))
    base_img = image.convert("RGBA").resize()
    fnt = ImageFont.truetype("Montserrat-Medium.ttf", 18)

    base_img_width, base_img_height = base_img.size

    img_obj = ImageDraw.Draw(base_img)
    img_obj.text(
        (base_img_width + 5, base_img_height / 2),
        text=text,
        font=fnt,
        fill=(0, 0, 0, 0),
    )

    return base_img
