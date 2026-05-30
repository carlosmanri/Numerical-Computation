# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:29:48 2019

@author: UO258425
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm


def derivatives_a(f,a,b,h):
    x = np.arange(a, b+h, h)
    df_c = np.zeros(len(x))
    
    for i in range(0,len(x)):
        df_c[i] = (f(x[i]+h)-f(x[i]-h))/(2*h)   
    
    df_c[0] = (f(x[0]+h)-f(x[0]))/h   #Progressive formula a
    df_c[-1] =(f(x[-1])-f(x[-1]-h))/h #Regressive formula a

    return x, df_c

def derivatives_b(f,a,b,h):
    x = np.arange(a, b+h, h)
    df_c = np.zeros(len(x))
    
    for i in range(0,len(x)):
        df_c[i] = (f(x[i]+h)-f(x[i]-h))/(2*h)   
    
    df_c[0] = (-3*f(x[0])+4*f(x[0]+h)-f(x[0]+2*h))/(2*h)   #Progressive order 2
    df_c[-1] = (f(x[-1]-2*h)-4*f(x[-1]-h)+3*f(x[-1]))/(2*h) #Regressive order 2

    return x, df_c

#%% Data    
f = lambda x: 1./x
df = lambda x: -1./x**2

a = 0.2
b = 1.2
h = 0.01

#%% Call the function
x, a_df_c = derivatives_a(f,a,b,h)
x, b_df_c = derivatives_b(f,a,b,h)

#%% Plot the derivatives
plt.plot(x, df(x), 'r', label="exact",linewidth=2.0)
plt.plot(x,a_df_c, 'b--', label="approximate A")

plt.legend()
plt.show()

plt.figure()

plt.plot(x, df(x), 'r', label="exact",linewidth=2.0)
plt.plot(x, b_df_c, 'b--', label="approximate B")

plt.legend()
plt.show()

#%% Print the global relative error
Ea_a = norm(df(x)-a_df_c)
Er_a = Ea_a / norm(df(x))
Ea_b = norm(df(x)-b_df_c)
Er_b = Ea_b / norm(df(x))
print("GLOBAL ERRORS")
print("h \t E(A_df) \t E(B_df)")
print(h,"\t%.6e" %Er_a,"\t%.6e" % Er_b)