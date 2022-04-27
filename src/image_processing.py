import numpy as np
from os import path
from PIL import Image
import io

def make_mask(image):
    if type(image) == bytes:
        wine_mask = np.array(Image.open(io.BytesIO(image)))
    else:
        wine_mask = np.array(Image.open(image))

    wine_mask[wine_mask == 0] = 255

    return wine_mask

def black_and_white(img_path):

    img = Image.open(img_path)

    thresh = 100

    fn = lambda x : 0 if x > thresh else 255

    bw_img = img.convert('L').point(fn, mode='1')

    with io.BytesIO() as output:
        bw_img.save(output, format="PNG")
        bw_img_io = output.getvalue()

    return bw_img_io

