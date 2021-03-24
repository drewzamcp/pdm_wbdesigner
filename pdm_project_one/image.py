#!/usr/bin/env python
from PIL import Image
import datetime as dt

COLOR_THRESHOLD = 190
FILE_DATE = dt.datetime.now().isoformat("-", "auto")


def create_bw_image(imagefile):

    img = Image.open(imagefile)
    rgba = img.convert("RGBA")
    datas = rgba.getdata()

    new_data = []
    for item in datas:
        if all(item > COLOR_THRESHOLD for item in item[:3]):
            row = (255, 255, 255, 0)
        else:
            row = (1, 1, 1, 0)
        new_data.append(row)

    output_path = "/Users/drewmac/webdev/pdm-project1/image_folder/processed/"
    outfile_name = f"processed_{FILE_DATE}_transparent.png"

    img.putdata(new_data)
    img.save(f"{output_path}{outfile_name}", "PNG")

    return img
