# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:36:04 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans


I = Image.open("holi.jpg")

a = np.asarray(I,dtype=np.float32)/255
plt.figure(figsize=(12,12))
plt.imshow(a)
plt.axis('off')
plt.show()

w, h = I.size
colors = I.getcolors(w * h)
num_colors = len(colors) 
num_pixels = w*h 
print ('Number of pixels = ', num_pixels)
print ('Number of colors = ', num_colors)


x, y, z = a.shape
print('a shape ', a.shape)
a1 = a.reshape(x*y, z)
print('a1 shape ', a1.shape)

# Apply KMeans
n = 10
k_means = KMeans(n_clusters=n)
k_means.fit(a1)
centroids = k_means.cluster_centers_
labels = k_means.labels_
print('centroids shape ', centroids.shape)
print('labels shape ', labels.shape)

a2 = centroids[labels]
print('a2 shape ', a2.shape)
a3 = a2.reshape(x,y,z)
print('a3 shape ', a3.shape)

plt.figure(figsize=(12,12))
plt.imshow(a3)
plt.axis('off')
plt.show()

# Save image
a4 = np.floor(a3*255)
a5 = a4.astype(np.uint8)
I1 = Image.fromarray(a5)
I1.save("holi2.jpg")

# Get total pixels and colors
w, h = I1.size
colors = I1.getcolors(w * h)
num_colors = len(colors) 
num_pixels = w*h 
print ('Number of pixels = ', num_pixels)
print ('Number of colors = ', num_colors)

plt.figure()
#################################################
## Now exercise 2 begins
#################################################
imgSize = 1000

# Throw away rgb values
colors = [x[0] for x in colors]
colors = np.sort(colors)


palette =  np.zeros((imgSize,imgSize))

for i in range(num_colors):
    for j in range(imgSize):
        for k in range(100):
            palette[k,j] = colors[i]
    


"""
# Fill the palette
for i in range(num_colors):
    colorMask = np.zeros_like((imgSize, imgSize/10))
    column = np.linspace(colors[i],colors[i],imgSize/10)
    colorMask = np.tile(column, (imgSize,1))

    palette = colorMask*palette
"""
    
# Show image
plt.imshow(palette)
plt.axis('off')
plt.show()
    

# Save the palette as image
imgPalette = palette.astype(np.uint8)
imgPalette = Image.fromarray(imgPalette)
imgPalette.save('colors.jpg')















