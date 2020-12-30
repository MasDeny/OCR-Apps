import pytesseract
import os
import sys

def read_image(image_path, lang="eng"):

    """
    Performs OCR in single image

    :path = str, path image file
    :lang = str, languange to be used while conversion (optional, default is english)

    Returns
    :text = str,  converted text from images

    """

    try:
        # img2 = Image.open(image_path)
        # text = pytesseract.image_to_string(img2)
        # print("fucker")
        # img = Image.open(path)
        # print(img)
        return pytesseract.image_to_string(image_path, lang=lang)
    except:
        return "[Error] Unable to Process the file: {0}".format(image_path)


# read_image("temp/temp.png")
