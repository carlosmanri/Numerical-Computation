# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:14:09 2019

@author: UO258425
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img  = Image.open("mickey.jpg")

img = img.convert('L')


a = np.asarray(img,dtype=np.float64)
plt.imshow(a,cmap='gray')
plt.show()

plt.figure()

py, px = np.gradient(a)
gr = np.sqrt(px**2+py**2)

plt.imshow(gr,cmap='gray')
plt.colorbar()
plt.show()

plt.figure()


b = gr > 50
plt.imshow(b*gr,cmap='gray')
plt.show()



