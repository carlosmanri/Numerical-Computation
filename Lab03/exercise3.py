# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:33:31 2019

@author: UO258425
"""
import numpy as np


def newton(f,df,x0, tol=1e-12, maxiter=100):
    x = 0
    k = 0
    xp = x0
    error = np.inf
    while (k < maxiter and error > tol):
        
        x = xp-(f(xp)/df(xp))        
        error = abs(x-xp)
        k+=1
    
    return (x, k)
    
      
    
    
f = lambda x: x**3-10*x**2+5
df = lambda x: 3*x**2 -20*x

(x,k) = newton(f,df,-0.7)
print("Solution =",x, "at iteration",k)


(x,k) = newton(f,df,0.7)
print("Solution =",x, "at iteration",k)

(x,k) = newton(f,df,9.9)
print("Solution =",x, "at iteration",k)