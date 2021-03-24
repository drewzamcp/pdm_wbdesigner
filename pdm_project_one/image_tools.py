#!/usr/bin/env python
from PIL import Image
import datetime as dt

COLOR_THRESHOLD = 180
FILE_DATE = dt.datetime.now().isoformat("-", "auto")


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
