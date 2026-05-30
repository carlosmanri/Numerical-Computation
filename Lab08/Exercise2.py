# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:44:42 2019

@author: UO258425
"""

from PIL import Image             # Python Imaging Library
import numpy as np                # Numerical Python 
import matplotlib.pyplot as plt   # Python plotting

img = Image.open('lena_gray_512.tif')

imgMatrix = np.asarray(img)

h = imgMatrix.shape[0]
w = imgMatrix.shape[1]
print("width = ", w)
print("height = ", h)

mask = np.zeros_like((h, w))

maskColumn = np.linspace(0,1,w)

print(maskColumn)

mask = np.tile(maskColumn, (h,1))

finalM = mask.T*imgMatrix

plt.imshow(finalM, cmap='gray')
plt.show()

#finalM *= 255
finalM = finalM.astype(np.uint8)

finalImg = Image.fromarray(finalM)
finalImg.save('Exercise2.png')
