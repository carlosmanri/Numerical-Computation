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
def derivatives(f,a,b,h):
    x = np.arange(a+h, b, h)
    df_f = np.zeros(len(x))
    df_b = np.zeros(len(x))
    df_c = np.zeros(len(x))
            
    for i in range(0,len(x)):
        
        df_f[i] = (f(x[i]+h)-f(x[i]))/h
        df_b[i] = (f(x[i])-f(x[i]-h))/h
        df_c[i] = (f(x[i]+h)-f(x[i]-h))/(2*h)    
    
    return x, df_f, df_b, df_c

#%% Data    
f = lambda x: np.exp(x)
df = lambda x: np.exp(x)

a = 0
b = 1
h = 0.1

#%% Call the function
x, df_f, df_b, df_c = derivatives(f,a,b,h)

#%% Plot the derivatives
plt.plot(x,df_f, 'b-', label="forward")
plt.plot(x,df_b, 'y-', label="backward")
plt.plot(x,df_c, 'g-', label="centered")
plt.plot(x, df(x), 'r--', label="exact")

plt.legend()
plt.show()

#%% Plot the errors
plt.figure()

plt.plot(x,abs(df(x)-df_b), 'y-', label='backward') # Backward derivative
plt.plot(x,abs(df(x)-df_f), 'b-', label='forward') # Backward derivative
plt.plot(x,abs(df(x)-df_c), 'g-', label='centered') # Backward derivative
plt.legend()
plt.show()

error_f = df(x)-df_f
error_b = df(x)-df_b
error_c = df(x)-df_c

#%% Print the global relative error
Ea_b = norm(df(x)-df_b)
Er_b = Ea_b / norm(df(x))
Ea_f = norm(df(x)-df_f)
Er_f = Ea_f / norm(df(x))
Ea_c = norm(df(x)-df_c)
Er_c = Ea_c / norm(df(x))

print("GLOBAL ERRORS")
print("h \t E(df_f) \t E(df_b) \t E(df_c)")
print(h,"\t%.6e" % Er_f,"\t%.6e" % Er_b,"\t%.6e" %Er_c,)















