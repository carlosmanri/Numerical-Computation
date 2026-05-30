# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:08:25 2019

@author: UO258425
"""

from PIL import Image             # Python Imaging Library
import numpy as np                # Numerical Python 
import matplotlib.pyplot as plt   # Python plotting

img = Image.open('lena_gray_512.tif')

imgMatrix = np.asarray(img)

mask = np.zeros_like((img.width, img.height))

# Center
cx = img.width/2
cy = img.height/2
radious = 150

y,x = np.ogrid[-cx:img.width-cx, -cy:img.height-cy]
mask = x*x + y*y <= radious*radious

array = np.zeros((img.width, img.height))
array[mask] = 1
imgFinal = imgMatrix*array
plt.imshow(imgMatrix*array, cmap='gray')
plt.show()

imgFinal = imgFinal.astype(np.uint8)
imgFinal = Image.fromarray(imgFinal)

imgFinal.save('Exercise1.jpg')

####### Exercise 1 part b
plt.figure()

img = Image.open('lena_gray_512.tif')

imgMatrix = np.asarray(img)

mask = np.zeros_like((img.width, img.height))

# Center
cx = img.width/2
cy = img.height/2
radious = 150

y,x = np.ogrid[-cx:img.width-cx, -cy:img.height-cy]
mask = x*x + y*y <= radious*radious

array = np.full((img.width, img.height),255/2)
array[mask] = 255
imgFinal = imgMatrix*array

imgFinal = np.interp(imgFinal,[0,np.max(imgFinal)],[0,255])

plt.imshow(imgFinal, cmap='gray')
plt.colorbar()
plt.show()

imgFinal = imgFinal.astype(np.uint8)
imgFinal = Image.fromarray(imgFinal)

imgFinal.save('Exercise1-b.jpg')












"""
Esperanza's class introduction code
"""

"""
i = Image.open('lena.jpg')
i1 = i.convert('L')

a = np.asarray(i)
a1 = np.asarray(i1, dtype=np.float64)

plt.imshow(a)
plt.show()

plt.figure()

plt.imshow(a1,cmap='gray')
plt.colorbar()
plt.show()

plt.figure()

gy,gx = np.gradient(a1)
a2 = - np.sqrt(gx**2+gy**2)

plt.imshow(a2, cmap='gray')
plt.colorbar()
plt.show()

plt.figure()

a3 = (a2-np.min(a2))/(np.max(a2)-np.min(a2)) # store as [0,1] img
a3 *= 255
a4 = a3.astype(np.uint8)
i2 = Image.fromarray(a4)
i2.save('lena_bw.jpg')
plt.imshow(a4, cmap='gray')
plt.colorbar()
plt.show()
"""
