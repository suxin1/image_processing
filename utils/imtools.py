import os
import numpy as np
import pylab as plt
from PIL import Image


def get_imlist(path):
    """
    Return a list of image file path which ends with '.jpg' in 'path'.
    :param path: A file path or directory
    :return: A list of image file path
    """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def convert2jpg(filelist):
    for infile in filelist:
        outfile = os.path.splitext(infile)[0] + ".jpg"
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print("cannot convert", infile)


def im_resize(im, sz):
    """
    Resize an image array.
    """
    pimage = Image.fromarray(im)
    return np.array(pimage.resize(sz))


def histeq(im, numbins=256):
    """ Histogram equalization of grayscale image. """
    # Get image histogram
    hist, bins = plt.histogram(im.flatten(), numbins, normed=True)
    cdf = hist.cumsum()     # Cumulative distribution function
    cdf = 255 * cdf / cdf[-1]

    # User linear interpolation of cdf to find new pixel values
    im2 = np.interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf


def compute_average(imlist):
    """ Compute the average of a list of images. """
    sum_im = np.array(Image.open(imlist[0]), 'f')
    num_of_im = 0
    for img in imlist[1:]:
        try:
            sum_im += np.array(Image.open(img), 'f')
            num_of_im += 1
        except:
            print(img + ' skipped.')

    averageim = sum_im / num_of_im
    return np.array(averageim, 'uint8')

