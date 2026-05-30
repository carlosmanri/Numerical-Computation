# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:30:12 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt

def debug(A,b,p):
    print("\nCoefficient matrix")
    print(A)
    print("\nRight hand side matrix")
    print(b)
    print("\nSystem solution")
    print(p)  
    
    return

def otherApproximate1(x,y,degree):
    #n = len(x)
    A = np.zeros((degree+1,degree+1))
    b = np.zeros(degree+1)
    #fill matrices
    for i in range(degree+1):
        for j in range(degree+1):
            A[i,j] = sum(x**(j+i))  
        b[i] = sum(x**i * y)
        
    #solve system
    p = np.linalg.solve(A,b)

    debug(A,b,p)
    
    return p[::-1]


f = lambda x: np.cos(np.arctan(x)) - np.exp(x**2)*np.log(x+2)
x = np.linspace(-1,1,10)
y = f(x)
degree = 4

p = otherApproximate1(x,y, degree)

xp = np.linspace(min(x), max(x))
yp = np.polyval(p,xp)
plt.plot(xp,yp,'b-', label='approximating polynomial')
plt.plot(x,y,'ro', label='nodes')
plt.legend();
plt.show()










































