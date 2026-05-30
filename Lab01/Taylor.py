# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 15:40:18 2019

@author: UO258425
"""
import numpy as np
f = lambda x: np.exp(x)

x0 = 0.5
pol = 0.
factorial = 1.

for i in range(3):
    term = x0**i/factorial
    pol += term
    factorial *= i+1
    
print("P3(0.5)     = ",pol)
print("np.exp(0.5) = ", np.exp(x0))

#%% Plot the polynomial
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.exp(x)

x = np.linspace(-1,1)
pol = 0.
factorial = 1.

for i in range(3):
    term = x**i/factorial
    pol += term
    factorial *= i+1
plt.plot(x, pol, label="P2")
plt.plot(x, f(x), label="f")
plt.legend()
plt.show()

#%% Plot the polynomial with function
import numpy as np
import matplotlib.pyplot as plt

def P(x0, degree):
    
    pol = 0.
    factorial = 1.
    
    for i in range(degree+1):
        term = x0**i/factorial
        pol += term
        factorial *= i+1
    
    return pol

f = lambda x: np.exp(x)
x = np.linspace(-3,3)
plt.plot(x, f(x), label="f")
        
for k in range(1,5):
    plt.plot(x, P(x,k), label="P2-"+str(k))
    
plt.legend()
plt.show()







