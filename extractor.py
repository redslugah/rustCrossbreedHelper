import pytesseract
import cv2
from PIL import Image, ImageGrab, ImageOps
import time
import numpy as np
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def image_read():
    # Grayscale, Gaussian blur, Otsu's threshold
    image = cv2.imread("rust.png")
    image = cv2.resize(image, (0, 0), fx=2, fy=2)

    # get (i, j) positions of all RGB pixels that are somewhat bright
    black_pixels = np.where(
        (image[:, :, 0] >= 130) &
        (image[:, :, 1] >= 130) &
        (image[:, :, 2] >= 130)
    )
    # set those pixels to black
    image[black_pixels] = [0, 0, 0]
    # cv2.imshow('first', image)
    # cv2.waitKey()

    # get (i, j) positions of all RGB pixels that are black (i.e. [0, 0, 0])
    black_pixels = np.where(
        (image[:, :, 0] != 0) &
        (image[:, :, 1] != 0) &
        (image[:, :, 2] != 0)
    )
    # set those pixels to white
    image[black_pixels] = [255, 255, 255]

    blur = cv2.GaussianBlur(image, (3, 3), 0)

    # Perform text extraction
    data = pytesseract.image_to_string(blur, config='--psm 11 -c tessedit_char_whitelist=WHYXG')
    # cv2.imshow('first', blur)
    # cv2.waitKey()
    data = re.sub('\W+', '', data)
    genetics = tuple(char for char in data)
    # print(genetics)
    return genetics


if __name__ == "__main__":
    image_read()
