# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:15:56 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt

def incrementalSearch(f,a,b,dx):
    x0 = a
    x1 = a+dx
    
    while(x1 <= b):
        if (f(x0)*f(x1) < 0):
            return (x0,x1)
        x0 = x1
        x1 += dx
        
    return (None,None)


def fixedPoint(g, x0, tol=1e-12, maxiter=200):
    error = np.inf
    k = 0
    x = 0
    xp = 0
    while (k < maxiter and error > tol):
        x = g(x)
        xp = x
        error = abs(x-xp)
        k+=1
        
        
    return (x, k)
    

f = lambda x: np.exp(-x) - x
g = lambda x: np.cos(x)
g2 = lambda x: 2*x-np.cos(x)
g3 = lambda x: x-((x-np.cos(x))/(1+np.sin(x)))
g4 = lambda x: (9*x+np.cos(x))/(10)




r = np.zeros(3)

i=0
(x0,x1) = incrementalSearch(f,-15,15,0.1)
while( x0 != None):
    print("There is a zero in [%.1f, %.1f]" % (x0,x1))
    (sol, k) = fixedPoint(g,x0,x1)
    r[i] = sol 
    print("Solution =",sol, "at iteration ",k)
    a = x1
    i+=1
    (x0,x1) = incrementalSearch(f,a,15,0.1)












