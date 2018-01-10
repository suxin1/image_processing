from PIL import Image
import numpy as np
import pylab as plt
from scipy.ndimage import filters
import os
from utils.imtools import get_imlist


imlist = get_imlist(os.getcwd() + "/images")


def derivatives(image):
    im = np.array(image.convert('L'))
    sigma = 1

    imx = np.zeros(im.shape)
    # filters.sobel(im, 1, imx)
    filters.gaussian_filter(im, (sigma, sigma), (0, 1), imx)

    imy = np.zeros(im.shape)
    # filters.sobel(im, 0, imy)
    filters.gaussian_filter(im, (sigma, sigma), (1, 0), imy)
    magnitude = np.sqrt(imx**2 + imy**2)
    # magnitude = 255 - magnitude

    plt.figure()
    plt.gray()
    plt.subplot(141)
    plt.imshow(im)

    plt.subplot(142)
    plt.imshow(imx)

    plt.subplot(143)
    plt.imshow(imy)

    plt.subplot(144)
    plt.imshow(magnitude)

    plt.show()


image = Image.open(imlist[3])

derivatives(image)