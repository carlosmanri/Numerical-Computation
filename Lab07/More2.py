# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:35:32 2019

@author: UO258425
"""

import numpy as np
import matplotlib.pyplot as plt


f1 = lambda x,y: x**2+y**2
f2 = lambda x,y: x**2-y**2
f = lambda x,y: (f1(x,y),f2(x,y))

hx = 0.1
hy = 0.1

x = np.arange(-2., 2. + hx, hx)
y = np.arange(-2., 2. + hy, hy)
x, y = np.meshgrid(x, y)

z1 = f1(x,y)
z2 = f2(x,y)

fy1, fx1 = np.gradient(z1,hx,hy)


fy2, fx2 = np.gradient(z2,hx,hy)


plt.figure()
plt.quiver(x, y, z1, z2)
plt.contour(x,y, fy2+fx1)
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.show()