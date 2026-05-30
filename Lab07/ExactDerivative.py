# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:36:32 2019

@author: UO258425
"""

import sympy as sym

x = sym.Symbol('x', real=True)

f_sim   = sym.sin(2*sym.pi*x)
df_sim  = sym.diff(f_sim,x)
d2f_sim = sym.diff(df_sim,x)

print(d2f_sim)


































