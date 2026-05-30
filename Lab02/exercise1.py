# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 15:04:11 2019

@author: UO258425
"""

import numpy as np


def horner(p, x0):
    q = np.zeros_like(p)
    
    q[0]=p[0]
    for i in range(1,len(p)):
        q[i] = p[i]+q[i-1]*x0
        
        
    return q

p = np.array([1, -1, 2, -3,  5, -2])
x0 = 1.


result = horner(p,x0)
q = result[:-1]
r = result[-1]
print("Q coefficients = ", q)
print("R(",x0,") = ", r)


p = np.array([ 5, -3,  1, -1, -4,  0,  0,  3])
x0 = -1.

result = horner(p,x0)
q = result[:-1]
r = result[-1]
print("Q coefficients = ", q)
print("R(",x0,") = ", r)
