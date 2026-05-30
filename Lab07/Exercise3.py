# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:08:22 2019

@author: UO258425
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

"""
First derivatives without the border
"""
def derivative2(f,a,b,h):
    x = np.arange(a+h, b-h, h) 
    d2f = np.zeros(len(x))
    
    for i in range(0,len(x)):
        d2f[i] = (f(x[i]+h)-2*f(x[i])+f(x[i]-h))/(h**2)   
        
    return x, d2f



#%% Data    
f = lambda x: np.sin(2*np.pi*x)
d2f = lambda x: -4*np.pi**2*np.sin(2*np.pi*x)

a = 0
b = 1
h = 0.01

#%% Call the function
x, df2_c = derivative2(f,a,b,h)

#%% Plot the derivatives
plt.plot(x, d2f(x), 'y', label="exact",linewidth=5.0)
plt.plot(x, df2_c, 'b--', label="approximate")

plt.legend()
plt.show()

#%% Print the global relative error
Ea = norm(d2f(x)-df2_c)
Er = Ea / norm(d2f(x))
print("GLOBAL ERRORS")
print("h \t E(A_df)")
print(h,"\t%.6e" % Er)

