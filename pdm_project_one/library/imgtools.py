#!/usr/bin/env python
import datetime as dt

from PIL import Image, ImageDraw, ImageFont
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import UploadFile

from pdm_project_one.settings import (
    IMG_OUTPUT_FLDR,
    FONT_FOLDER,
)

COLOR_THRESHOLD = 200
FILE_DATE = dt.datetime.now().isoformat("-", "auto")
MAX_HEIGHT = 51
MAX_WIDTH = 720
MAX_SIZE = (MAX_WIDTH, MAX_HEIGHT)


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

    outfile_name = f"{IMG_OUTPUT_FLDR}/tmp_transparent.png"

    rgba.putdata(new_data)
    rgba.save(f"{outfile_name}", "PNG", quality=2)

    return rgba


def add_text_image(image: Image, text: str):

    base_layer = Image.new("RGBA", (MAX_WIDTH, MAX_HEIGHT), (255, 255, 255, 0))
    base_img = image.copy()
    base_img.thumbnail(MAX_SIZE)
    base_layer.alpha_composite(base_img)
    fnt = ImageFont.truetype(f"{FONT_FOLDER}/Poppins-Medium.ttf", 22)

    d = ImageDraw.Draw(base_layer)
    d.text(
        (base_img.width + 5, base_layer.height / 2),
        text=text,
        font=fnt,
        fill=(0, 0, 0, 255),
        anchor="lm",
    )

    base_layer.save(f"{IMG_OUTPUT_FLDR}/tmp_joined.png")

    return base_layer


def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path
