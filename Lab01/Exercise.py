# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:17:38 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt

def approx_Equal(x, y, tolerance=1.e-6):
    return abs(x-y) <= 0.5 * tolerance * (x + y)

tolerance = 1.e-6
maxNumSum = 100

f = lambda x: np.exp(x)
x = np.linspace(-1,1)


def P(x0, degree):
    
    pol = 0.
    factorial = 1.
    
    for i in range(degree+1):
        term = x0**i/factorial
        pol += term
        factorial *= i+1
    
    return pol


i = 1
value = 0
print(approx_Equal(value, f(x), tolerance))

while i<maxNumSum or (value-f(-0.5)>tolerance) :
    print(approx_Equal(value, f(x), tolerance))

    value = P(-0.5, i)
    i+=1

print("Function value in -0.5      =",f(-0.5))
print("Approximation value in -0.5 =",value)
print("Number of iterations:       =", i)
