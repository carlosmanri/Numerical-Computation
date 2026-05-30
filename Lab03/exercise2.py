# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:52:23 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt

def incrementalSearch(f,a,b,dx):
    x0 = a
    x1 = a+dx
    
    while(x1 <= b):
        if sign(f(x0)) != sign(f(x1)):
            return (x0,x1)
        x0 = x1
        x1 += dx
        
    return (None,None)
      
   
def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1
   
    
def bisection(f, a ,b ,tol = 1e-12, maxiter = 100):
    a1 = a
    b1 = b
    k = 0
    x = (a1+b1)/2
    error = np.inf

    while( k < maxiter and error > tol ):
        if(sign(f(a1)) != sign(f(x))):
            b1 = x
        elif(sign(f(x)) != sign(f(b1))):
            a1 = x
        else: #found 0
            return (x, k)
        xp = x
        x = (a1+b1)/2
        error = abs(x-xp)
        k+=1
    
    return (x, k)
    

 
############################################################### 
f = lambda x : x**3 - 10*x**2 + 5  # define the function

r = np.zeros(3)
i = 0

dx = 0.1
a = -15
b = 15  


(x0,x1) = incrementalSearch(f,a,b,dx)
while( x0 != None):
    print("There is a zero in [%.1f, %.1f]" % (x0,x1))
    (sol, k) = bisection(f,x0,x1)
    r[i] = sol 
    print("Solution =",sol, "at iteration ",k)
    a = x1
    i+=1
    (x0,x1) = incrementalSearch(f,a,b,dx)


x = np.linspace(-15,15)             # define the mesh in (-1,2)
OX = 0*x 

plt.plot(x,f(x))                # plot the function
plt.plot(x,OX,'k-')             # plot the X axis
plt.show()
plt.plot(r,r*0,'ro')
