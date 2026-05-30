# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:16:22 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt


def lagrange_fundamental(x,k,z):
    
    yz = 1.
    
    for i in range(0, len(x)):
        if( i != k):
            yz *=(z-x[i])/(x[k]-x[i])
        
    return (z,yz)


def lagrange_polynomial(x,y,z):
    pz = np.zeros(len(x))
    for i in range(0, len(x)):
        pz += y[i]*lagrange_fundamental(x,i,z)
    
    return



x = np.array([2.,3.,4.,5.,6.])
y = np.array([2.,6.,5.,5.,6.])


z = np.linspace(min(x), max(x))



for i in range(0, len(x)):
    (z, yz) = lagrange_fundamental(x,i,z)
    plt.plot(z,yz)
    
    
plt.plot(x,y,'ro')    
"""
xp = np.linspace(min(x),max(x))
yp = np.polyval(yz,xp)
plt.plot(xp,yp)
"""
(z, yz) = lagrange_fundamental(x,2,z)
plt.plot(z,yz)


plt.legend(['nodes','polynomial'], loc= 'best')
plt.show()



#######


"""
k = 2
z = np.linslace(min(x), max(x))
yz = 1.
n = len(x)
for i in range(n):

"""




