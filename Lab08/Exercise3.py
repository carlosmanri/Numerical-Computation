# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:36:14 2019

@author: UO258425
"""
from PIL import Image             # Python Imaging Library
import numpy as np                # Numerical Python 
import matplotlib.pyplot as plt   # Python plotting

squareSize = 250
imgSize = 2000

chess = np.zeros((squareSize,squareSize))


pattern = np.ones((squareSize*2, squareSize*2))

for i in range(squareSize,squareSize*2):
    for j in range(squareSize):
        pattern[i,j] = 0

for i in range(squareSize):
    for j in range(squareSize, squareSize*2):
        pattern[i,j] = 0

chess = np.tile(pattern, (4,4))

plt.imshow(chess,cmap='gray')
plt.colorbar()
plt.show()

chess *= 255
chess = chess.astype(np.uint8)

imgChess = Image.fromarray(chess)

imgChess.save('chess.png')

#################################################################
#                       Exercise 2 B
#################################################################

imgSize = 500
circunferenceWide = 10

circles = np.zeros((imgSize,imgSize))

cx = imgSize/2
cy = imgSize/2
r = imgSize/2 -10

y,x = np.ogrid[-cx:imgSize-cx, -cy:imgSize-cy]
color = 0

while (r>= 10):
    mask = x*x + y*y <= r*r
    
    circles[mask] = 1 if color%2==0 else 0

    r-=10
    color = 1 if color%2==0 else 0


plt.figure()
plt.imshow(circles, cmap='gray')
plt.show()


circles *= 255
circles = circles.astype(np.uint8)

circlesImg = Image.fromarray(circles)

circlesImg.save('circles.png')























