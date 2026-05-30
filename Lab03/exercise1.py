# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:23:45 2019

@author: UO258425
"""

f = lambda x : x**3 - 10*x**2 + 5  # define the function

def incrementalSearch(f,a,b,dx):
    x0 = a
    x1 = a+dx
    
    while(x1 <= b):
        if sign(f(x0)) != sign(f(x1)):
            return (x0,x1)
        x0 = x1
        x1 += dx
        
    return (None,None)
      
   
def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1
   
    
dx = 0.1
a = -15
b = 15  

(x0,x1) = (0,0) 
while((x0,x1) != (None,None)):
    
    (x0,x1) = incrementalSearch(f,a,b,dx)
    if((x0,x1) != (None, None)):
        print("There is a zero in [%.1f, %.1f]" % (x0,x1))
    else:
        print("There is no solution")  
    a = x1


    



    
    