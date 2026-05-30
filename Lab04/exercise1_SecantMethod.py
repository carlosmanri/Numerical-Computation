# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:52:42 2019

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


def secant(f, x0, x1, tol=1e-12, maxiter=100):
    error = np.inf
    k = 0
    x = 0
    xp = 0
    xp2 = x0
    
    x = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
    
    while(k < maxiter and error > tol):
        xp2 = xp
        xp = x
        x =   xp -f(xp)*((xp-xp2)/(f(xp)-f(xp2)))

        error = abs(x-xp)
        k+=1
        
    return (x, k)

    
f = lambda x: x**3 -10*x**2 + 5
r = np.zeros(3)


i=0
(x0,x1) = incrementalSearch(f,-15,15,0.1)
while( x0 != None):
    print("There is a zero in [%.1f, %.1f]" % (x0,x1))
    (sol, k) = secant(f,x0,x1)
    r[i] = sol 
    print("Solution =",sol, "at iteration ",k)
    a = x1
    i+=1
    (x0,x1) = incrementalSearch(f,a,15,0.1)




a = -1.; b = 11;
x = np.linspace(a, b, 200)  
plt.plot(x, f(x),'b-', label='f')
plt.plot(x, 0*x,'k-')              
plt.plot(r,r*0,'ro')    
plt.legend(loc='best')
plt.show()