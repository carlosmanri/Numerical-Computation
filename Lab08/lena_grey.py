# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:03:37 2019

@author: UO258425
"""

from PIL import Image             # Python Imaging Library
import numpy as np                # Numerical Python 
import matplotlib.pyplot as plt   # Python plotting

img = Image.open('lena.jpg')

#img.show()

plt.imshow(np.asarray(img))
plt.show()

plt.figure()

print (img.size, img.mode, img.format)

imgbw = img.convert('L') # 'L' for gray scale mode
print (imgbw.mode)

plt.imshow(np.asarray(imgbw), cmap='gray')
plt.show()



imgbw.save('lena_gray.tif')