# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:50:44 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt

def hornerVect(p, x):
    Q = np.zeros((len(x),len(p)))
    Q[:,0] = np.ones_like(x)*p[0]
    
    y = np.zeros_like(x)
    q = np.zeros_like(p)

    
    for i in range(len(x)):
        
        q[0]=p[0]
        for j in range(1,len(p)):
                
            q[j] = p[j]+q[j-1]*x[i]
        
        y[i] = q[-1]
        
        
    return Q[:,-1]

p = np.array([1., -1., 2., -3., 5., -2.])
x = np.linspace(-1,1)
OX = 0*x  
                      
plt.plot(x,hornerVect(p,x), label = 'p')
plt.plot(x,OX,'k') 
plt.title('Horner: proposed 1') 
plt.legend()   
plt.show()
