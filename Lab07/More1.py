# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:14:45 2019

@author: UO258425
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm # colormap


f = lambda x,y: x*np.exp(-(x**2) - (y**2))
hx = 0.1
hy = 0.1

x = np.arange(-2., 2. + hx, hx)
y = np.arange(-2., 2. + hy, hy)
x, y = np.meshgrid(x, y)
z = f(x,y)

plt.contour(x, y, z, 20, cmap=cm.bwr)
plt.title('f(x,y) = xe^(-x^2 -y^2)', fontsize=16)
plt.show()

fig = plt.figure(figsize=(10,5))
ax = fig.gca(projection='3d')
ax.plot_surface(x, y, z, cmap=cm.bwr)
plt.title('f(x,y) = xe^(-x^2 -y^2)', fontsize=16)
plt.show()

plt.figure()

plt.contour(x, y, z, 20, cmap=cm.bwr)

fy, fx = np.gradient(z,hx,hy)

plt.quiver(x,y, fx,fy)
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.show()

