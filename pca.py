from PIL import Image
from PCV.tools.pca import pca
from utils.imtools import *
import pylab as plt
import numpy as np


imlist = get_imlist(os.getcwd() + '/images/fontimages/a_thumbs')

# Open one image to get size
im = np.array(Image.open(imlist[0]))
m, n = im.shape[0:2]
imnbr = len(imlist)

# Create matrix to store all flatted images
immatrix = np.array([np.array(Image.open(impath)).flatten() for impath in imlist], 'f')

# Perform PCA
V, S, immean = pca(immatrix)

# Show some images
plt.figure()
plt.gray()
plt.subplot(241)
plt.imshow(immean.reshape(m, n))
for i in range(7):
    plt.subplot(2, 4, i + 2)
    plt.imshow(V[i].reshape(m, n))

plt.show()
