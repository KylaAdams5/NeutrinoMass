'''Program to draw a random unifor distribution using the Box-Muller Method in two methods
-the first is computationally expensive
-the second is quicker

-program design to be edited with a text editor and run in the ipython notebook


'''
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from math import *
mean = 0
sigma = 1
size = 15
dist = np.zeros(size)
dist2 = np.zeros(size)

x = np.zeros(size)

for i in range(len(dist)):
    x[i] = i+1
    i+1

    # Method 1
for i in range(len(dist)-1):
    x1 = np.random.uniform()
    x2 = np.random.uniform()

    y1 = sqrt(-2*np.log(x1))*np.cos(2*pi*x2)
    y2 = sqrt(-2*np.log(x1))*np.sin(2*pi*x2)

    z1 = mean + sigma*y1
    z2 = mean + sigma*y2
    dist[i] = z1
    dist[i+1] = z2
    i = i+2
# print(dist)

# plt.hist(dist)
# plt.show()

# Method 2
for i in range(len(dist)-1):
    x1 = np.random.uniform()
    x2 = np.random.uniform()

    u1 = (2*x1) -1
    u2 = (2*x2)-1

    d = u1**2 - u2**2
    if d > 1:
        u1 = 0
        u2 = 0
    elif  d < 0:
        u1 = 0
        u2 = 0
    else:
        y1 = u1*sqrt((-2*np.log(d))/d)
        y2 = u2*sqrt((-2*np.log(d))/d)

        z1 = mean + sigma*y1
        z2 = mean + sigma*y2
    dist2[i] = z1
    dist2[i+1] = z2
    i = i+2

print(min(dist2), max(dist2), '\n' , dist2)
# plt.hist(dist2)#, bins = 500)
# plt.show()
