from scipy.ndimage import morphology, measurements
from PIL import Image
import numpy as np
import pylab as plt
import os

parent_dir = os.path.split(os.getcwd())[0]
# im = np.array(Image.open(os.getcwd() + '/images/data/ceramic-houses_t0.png').convert('L'))
im = np.array(Image.open(os.getcwd() + '/images/data/houses.png').convert('L'))
im = 1 * (im < 128)

im2  = morphology.binary_opening(im, np.ones((9, 5)), iterations=2)

lable, num_object = measurements.label(im2)

plt.gray()
plt.imshow(im2)
plt.title('Number of object: {}'.format(num_object))

plt.figure()
plt.imshow(lable)

plt.show()
