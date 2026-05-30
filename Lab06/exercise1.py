# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:05:23 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision = 2)   # only 2 fractionary digits
np.set_printoptions(suppress = True) # do not use exponential notation


def approximate1(x,y,degree):
    V = Vandermonde(x,degree)
    #coefficient matrix
    A = np.dot(V.T, V)
    b = np.dot(V.T, y)
    #solve system
    p = np.linalg.solve(A,b)
 
    return p[::-1]


def Vandermonde(x, degree):
    n = len(x)
    V = np.ones((n,n))
    for j in range(1,n):
        V[:,j] = x**j
    return V

def polVandermonde(x,y):
    
    V = Vandermonde(x);
    p = np.linalg.solve(V,y)
    p = p[::-1] #flip
    
    return p


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


#############################################################

f = lambda x: np.cos(x)
x = np.linspace(-1,1,5)    
y = f(x)
degree = 2


p = otherApproximate1(x,y, degree)

xp = np.linspace(min(x), max(x))
yp = np.polyval(p,xp)
plt.plot(xp,yp,'b-', label='approximating polynomial')
plt.plot(x,y,'ro', label='nodes')
plt.legend();
plt.show()




 

