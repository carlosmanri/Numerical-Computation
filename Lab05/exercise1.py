# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:56:50 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt

def polVandermonde(x,y):
    
    V = Vandermonde(x);
    p = np.linalg.solve(V,y)
    p = p[::-1] #flip
    
    return p
    

def Vandermonde(x):
    n = len(x)
    V = np.ones((n,n));
    
    f = lambda x,y: x**y
    V[:,0] = np.ones(n); #first column are ones
    for i in range(1,n):
        V[:,i] = f(x,i)
  
                
    return V

x = np.array([2.,3.,4.,5.,6.])
y = np.array([2.,6.,5.,5.,6.])

x1 = np.array([0.,1.,2.,3.,4.,5.,6.])
y1 = np.array([3.,5.,6.,5.,4.,4.,5.])


np.set_printoptions(precision = 2)   # only 2 fractionary digits
np.set_printoptions(suppress = True) # do not use exponential notation


V = Vandermonde(x)
print('V matrix')
print(V)
pol = polVandermonde(x,y)
print('pol Polynomial coefficients')
print(pol)

V1 = Vandermonde(x1)
print('V1 matrix')
print(V1)
pol1 = polVandermonde(x1,y1)
print('pol1 Polynomial coefficients')
print(pol1)


va = np.vander(x, len(x))
print(va)


plt.plot(x,y,'ro')
plt.plot(x1,y1,'go')
plt.show()

xp = np.linspace(min(x),max(x))
yp = np.polyval(pol,xp)
plt.plot(xp,yp)
xp1 = np.linspace(min(x1),max(x1))
yp1 = np.polyval(pol1,xp1)
plt.plot(xp1,yp1)
