# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:31:34 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def debug(A,b,p):
    print("\nCoefficient matrix")
    print(A)
    print("\nRight hand side matrix")
    print(b)
    print("\nSystem solution")
    print(p)  
    
    return

def approximate1(x,y,degree):
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

def approximate2(f,a1,b1,degree):
    #n = len(x)
    A = np.zeros((degree+1,degree+1))
    b = np.zeros(degree+1)
    #fill matrices
    for i in range(degree+1):
        for j in range(degree+1):
            g = lambda x: x**(j+i)
            A[i,j] = quad(g,a1,b1)[0] 
        h = lambda x: x**i * f(x)
        b[i] =  quad(h,a1,b1)[0]
        
    #solve system
    p = np.linalg.solve(A,b)

    debug(A,b,p)
    
    return p[::-1]



###########################################################

f = lambda x: np.cos(np.arctan(x)) - np.exp(x**2)*np.log(x+2)

a1 = -1
b1 = 1
degree = 4

p = approximate2(f, a1, b1, degree)

xp = np.linspace(a1, b1)
yp = np.polyval(p,xp)
plt.plot(xp,yp,'b-', label='approximating polynomial')
plt.plot(xp,f(xp),'r-', label='function')
plt.legend();
plt.show()

Er = np.linalg.norm(yp-f(xp))/np.linalg.norm(f(xp))

print("The error is = ", Er)
