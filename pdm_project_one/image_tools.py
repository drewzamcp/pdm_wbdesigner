#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import datetime as dt

COLOR_THRESHOLD = 200
FILE_DATE = dt.datetime.now().isoformat("-", "auto")
MAX_HEIGHT = 51
MAX_WIDTH = 720
MAX_SIZE = (MAX_WIDTH, MAX_HEIGHT)

TMP_FOLDER = "tmp_img_folder"


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

    outfile_name = f"{TMP_FOLDER}/tmp_transparent.png"

    rgba.putdata(new_data)
    rgba.save(f"{outfile_name}", "PNG", quality=2)

    return rgba


def add_text_image(image: Image, text: str):

    base_layer = Image.new("RGBA", (MAX_WIDTH, MAX_HEIGHT), (255, 255, 255, 0))
    base_img = image.copy()
    base_img.thumbnail(MAX_SIZE)
    base_layer.alpha_composite(base_img)
    fnt = ImageFont.truetype("fonts/Poppins-Medium.ttf", 22)

    d = ImageDraw.Draw(base_layer)
    d.text(
        (base_img.width + 5, base_layer.height / 2),
        text=text,
        font=fnt,
        fill=(0, 0, 0, 255),
        anchor="lm",
    )

    base_layer.save(f"{TMP_FOLDER}/tmp_joined.png")

    return base_layer
