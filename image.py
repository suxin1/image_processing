import os
from PIL import Image
import numpy as np
import matplotlib.pylab as plt
from utils.imtools import get_imlist, histeq, compute_average


imagelist = get_imlist(os.getcwd() + '/images')
ssimagelist = get_imlist(os.getcwd() + '/images/square_images')

def crop_and_rotate(image):

    """
    Select a region and rotate
    """
    box = [200, 200, 600, 600]
    region = image.crop(box).convert('L')
    region = region.transpose(Image.ROTATE_180)
    image.paste(region, box)

    aimage = np.array(image)

    plt.imshow(aimage)


def contour(image):
    """
    contour plot
    """
    plt.figure()
    image = image.convert('L')
    plt.gray()
    plt.contour(image, origin='image')
    plt.axis('equal')


def gray(image):
    """
    plot gray image
    :param image: PIL.Image object
    :return:
    """
    plt.figure()
    image = image.convert('L')
    aimage = np.array(image)
    print(aimage.shape, aimage.dtype)
    plt.gray()
    plt.imshow(np.array(aimage))


def histgram(image):
    """
    Histogram plot
    @:param image: PIL.Image object
    """
    plt.figure()
    acimage = np.array(image.convert('L'))
    plt.hist(acimage.flatten(), 128)


def interaction():
    """
    Interaction with plots
    """
    print("Please click 3 points")
    x = plt.ginput(3)
    print("you clicked: ", x)


def array_manipulate(image):
    aimage = np.array(image.convert('L'))
    ai_image = 255 - aimage                     # f(x) = 255 - x
    ac_image = (100.0/255) * aimage + 100       # f(x) = (100 / 255)* x + 100
    aq_image = 255.0 * (aimage/255.0)**2        # f(x) = 255 * (x/255)
    plt.figure()
    plt.gray()

    plt.subplot(311)
    plt.imshow(ai_image)
    plt.axis('off')

    plt.subplot(312)
    plt.imshow(ac_image)
    plt.axis('off')

    plt.subplot(313)
    plt.imshow(aq_image)
    plt.axis('off')


def im_hist_eq(image):
    aimage = np.array(image.convert('L'))
    ae_image, cdf = histeq(aimage)

    plt.figure()
    plt.gray()

    plt.subplot(231)
    plt.hist(aimage.flatten(), bins=256)

    plt.subplot(233)
    plt.hist(ae_image.flatten(), bins=256)

    plt.subplot(234)
    plt.imshow(aimage)
    plt.axis('off')

    plt.subplot(232)
    plt.plot(cdf, 'r-')

    plt.subplot(236)
    plt.imshow(ae_image)
    plt.axis('off')


def im_hist_eq_2(image):
    aimage = np.array(image.convert('L'))
    ae_image, cdf = histeq(aimage)

    plt.figure()
    plt.gray()

    plt.subplot(211)
    plt.imshow(aimage)

    plt.subplot(212)
    plt.imshow(ae_image)
    plt.axis('off')


def average(imlist):
    aimage = compute_average(imlist)

    plt.imshow(aimage)


image = Image.open(imagelist[0])

average(ssimagelist)

plt.show()
