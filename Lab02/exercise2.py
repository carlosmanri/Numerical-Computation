# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:19:15 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt

def hornerV(p, x):
    y = np.zeros_like(x)
    q = np.zeros_like(p)

    
    for i in range(len(x)):
        
        q[0]=p[0]
        for j in range(1,len(p)):
                
            q[j] = p[j]+q[j-1]*x[i]
        
        y[i] = q[-1]
        
        
    return y

p = np.array([1., -1., 2., -3., 5., -2.])
r = np.array([5., -3., 1., -1., -4., 0., 0., 3.])
x = np.linspace(-1,1)
OX = 0*x  
                      
plt.plot(x,hornerV(p,x), label = 'p')
plt.plot(x,hornerV(r,x), label = 'r')
plt.plot(x,np.polyval(p,x), label = 'polyval(p)')
plt.plot(x,OX,'k') 
plt.title('Horner: exercise 2') 
plt.legend()   
plt.show()



