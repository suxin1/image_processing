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
    num_of_im = 1
    for img in imlist[1:]:
        try:
            sum_im += np.array(Image.open(img), 'f')
            num_of_im += 1
        except:
            print(img + ' skipped.')

    averageim = sum_im / num_of_im
    return np.array(averageim, 'uint8')


def crop_image(imname, box):
    """
    Image Crop
    :param imname: String, File path of an image
    :param size: [x1, y1, x2, y2]
    :return:
    """
    image = Image.open(imname)
    imcropped = image.crop(box)
    strsize = '_' + str(box[2] - box[0]) + '_' + str(box[3] - box[1])
    rename = os.path.splitext(imname)[0] + strsize + '.jpg'
    try:
        imcropped.save(rename)
    except IOError:
        print("Can't crop image " + imname)


def select_crop(impath):
    image = Image.open(impath)

    aimage = np.array(image)
    plt.figure()
    plt.imshow(aimage)
    points = plt.ginput(2)
    box = np.array(points, 'i').flatten()

    crop_image(impath, box)