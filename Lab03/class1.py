# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:03:32 2019

@author: UO258425
"""



import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(-1,2)             # define the mesh in (-1,2)
f = lambda x : x**3 - 2*x**2 + 1  # define the function
OX = 0*x                          # define X axis



plt.plot(x,f(x))                # plot the function
plt.plot(x,OX,'k-')             # plot the X axis
plt.show()


a=234.
b=-1231.
print("a = ",bin(a))
print("b = ",bin(b))
print("a>>31 = ",bin(a>>31))
print("b>>31 = ",bin(b>>31))

if((a>>31 ^ b>>31) ):
    print("a sign different from b")


    