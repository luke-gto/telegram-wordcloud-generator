from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import cv2


def make_mask(image): # converts a png supposedly ready to be used as a mask to a np array

    wine_mask = np.array(Image.open(image))

    return wine_mask


def black_and_white(img_path): # converts a random PNG to a grayscale img and then to a b/w image then it becomes an array ready to be used as a mask

    image = cv2.imread(img_path)

    grayImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    (thresh, bw_img) = cv2.threshold(grayImage, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    bw_img_inverted = cv2.threshold(grayImage, thresh, 255, cv2.THRESH_BINARY)[1]

    bw_img = np.invert(bw_img_inverted)

    return bw_img

