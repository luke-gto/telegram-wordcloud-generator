import numpy as np
from os import path
from PIL import Image
import io
from matplotlib import pyplot as plt


def make_mask(image):

    if type(image) == bytes:

        wine_mask = np.array(Image.open(io.BytesIO(image)))
        plt.imshow(wine_mask, interpolation='bilinear')
        plt.show()


    else:
        wine_mask = np.array(Image.open(image))

    return wine_mask

def black_and_white(img_path):

    img = Image.open(img_path)

    thresh = 100

    fn = lambda x : 0 if x > thresh else 255

    bw_img = img.convert('L').point(fn, mode='1')

    with io.BytesIO() as output:
        bw_img.save(output, format="png")
        bw_img_io = output.getvalue()

    return bw_img_io

