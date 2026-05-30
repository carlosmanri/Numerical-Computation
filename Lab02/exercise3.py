# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:22:59 2019

@author: UO258425
"""
import numpy as np

def polDer(p, x0):
    derivatives = np.zeros_like(p)    
    q = np.zeros_like(p)
    factorial = 1
    
    for i in range(len(derivatives)):
        
        q[0]=p[0]
        for j in range(1, len(q)):
            q[j] = p[j]+q[j-1]*x0
        
        derivatives[i] = q[-1]*factorial 
        p = q[:-1]
        q = np.zeros_like(p)
        factorial *= i+1
        
        
    return derivatives

p = np.array([1, -1, 2, -3, 5, -2])
x1 = 1.
print("Derivatives of P in x0 = ", x1)
print(polDer(p,x1))


r = np.array([ 5, -3,  1, -1, -4,  0,  0,  3])
x1 = -1.
print("Derivatives of R in x0 = ", x1)
print(polDer(r,x1))



