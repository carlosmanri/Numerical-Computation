# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:15:12 2019

@author: UO258425
"""

import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------
# Define f
f = lambda x: np.exp(x)
#--------------------------------------
# Define the polynomials
def P(x0,degree):
    polynomial = 0.
    factorial = 1.

    for i in range(degree + 1):
        term = x0**i/factorial
        polynomial += term
        factorial *= i+1

    return polynomial 
#--------------------------------------
a = -3.; b = 3.
x = np.linspace(a,b)
OX = 0*x                               

plt.plot(x,f(x), label = 'f')
plt.plot(x,OX,'k') 

for degree in range(1,7):
    plt.plot(x,P(x,degree), label = 'P'+str(degree))
    plt.title('Function and approximation polynomials') 
    plt.legend()   
    plt.pause(2)                        
plt.show()
