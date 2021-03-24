#! user/env/python
from PIL import Image, ImageOps
from pdm_project_one import image


def main():  # sourcery skip: inline-immediately-returned-variable
    bw_img = wristband_image(
        "/Users/drewmac/webdev/pdm-project1/image_folder/raw/Northern Farm.jpg"
    )
    return bw_img


def wristband_image(img_path):
    """
    Starting point for most artworks. Handles the conversion of different
    image versions (*.png, *.jpg, *.pdf)
    """
    # upload image in supported format (*.png, *.jpg, *.pdf)
    # convert the image to black and white bitmap
    # remove background
    # resize to fit wristand
    # return processed image
    bw_img = image.create_bw_image(img_path)
    new_img = cImage.open(bw_img)
    new_img = new_img.convert("RGBA")
    # img = img.convert("RGBA")

    # _bw_img = get_bw_image(img=img)
    # cropped_img = remove_white_background(bw_img=_bw_img)

    return new_img


# def get_bw_image(img):
#     fn = lambda x: 255 if x > COLOR_THRESHOLD else 0
#     img = img.convert("L").point(fn, mode="1")
#     return img.convert("RGBA")


# def remove_white_background(img):
#     rgba_img = img.convert("RGBA")
#     return ImageOps.invert(rgba_img)


if __name__ == "__main__":
    main()
