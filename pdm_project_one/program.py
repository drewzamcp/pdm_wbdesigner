#! user/env/python
from pdm_project_one import image_tools


def main():  # sourcery skip: inline-immediately-returned-variable
    text_input = str(input("Enter text for wristband: "))
    transparent_img = wristband_image(
        "/Users/drewmac/webdev/pdm-project1/image_folder/raw/Northern Farm.jpg",
        text_input,
    )
    return transparent_img


def wristband_image(img_path, input_text: str):
    """
    Starting point for most artworks. Handles the conversion of different
    image versions (*.png, *.jpg, *.pdf)
    """
    # upload image in supported format (*.png, *.jpg, *.pdf)
    # convert the image to black and white bitmap
    # remove background
    transparent_image = image_tools.get_transparent_image(img_path)
    merged_image = image_tools.add_text_image(transparent_image, input_text)
    # resize to fit wristand

    return merged_image


if __name__ == "__main__":
    main()
