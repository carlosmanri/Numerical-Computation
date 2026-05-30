# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:20:34 2019

@author: UO258425
"""

import sympy as sym
import numpy as np
import scipy.optimize as op
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




x = sym.Symbol('x', real=True)

f_sim   = x**3 + sym.log((x + 7))*sym.cos(4*x)-1
df_sim  = sym.diff(f_sim,x)
d2f_sim = sym.diff(df_sim,x)


f   = sym.lambdify([x], f_sim,'numpy') 
df  = sym.lambdify([x], df_sim,'numpy') 
d2f = sym.lambdify([x], d2f_sim,'numpy') 



r = np.zeros(4)
i=0
(x0,x1) = incrementalSearch(df,-2,15,0.1)
while( x0 != None):
    r[i] = op.newton(df,x0,tol=1e-12, maxiter=100) 
    print("d2f(",i,") =",r[i])
    a = x1
    i+=1
    (x0,x1) = incrementalSearch(df,a,15,0.1)



x = np.linspace(-2,2,1000)
plt.plot(x,df(x))
plt.plot(r,r*0,'ro')    
plt.legend(['df'],loc='best')
plt.plot([-2,2],[0,0],'k-')
plt.show()

plt.figure(2)

maxi = r[[0,2]]
mini = r[[1,3]]

x = np.linspace(-2,2,1000)
plt.plot(x,f(x))
plt.plot(maxi,f(maxi),'go')  
plt.plot(mini,f(mini),'ro')  
 
plt.legend(['f','max','min'],loc='best')
plt.plot([-2,2],[0,0],'k-')
plt.show()


