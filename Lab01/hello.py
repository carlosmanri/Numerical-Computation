# -*- coding: utf-8 -*-
#%% Exponential
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.exp(x)
x = np.linspace(-1,1)
y = f(x)

ox = np.zeros_like(x)
plt.plot(x,y, label = 'f')
plt.plot(x,ox,'k',label='OX axis')
plt.title('Exponential function')
plt.legend()
plt.savefig('test.png')
plt.show()





#%% Vectorization time exec example
import time
z = np.linspace(-1,1,1000000)
yz = np.zeros_like(z)

t0 = time.time()
for i in range(len(z)):
    yz[i] = f(z[i])
t1 = time.time()
t = t1-t0
print('Time elapsed: ', t)


t0 = time.time()
yz = f(z)#<--- Vectorization
t1 = time.time()
t = t1-t0
print('Time elapsed: ', t)












