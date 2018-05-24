'''
Kyla Adams
PHYC20007

Program to draw a random unifor distribution using the Box-Muller Method in two methods
-the first is computationally expensive

-the second is quicker - used in the notebook

- program design to be edited with a text editor and run in the ipython notebook


'''
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from math import *

# initialise variables and arrays
mean = 1
sigma = 20
size = 10000

dist = np.ones(size)
dist2 = np.ones(size)

plotx = np.ones(size)
x = np.ones(size)
y = np.ones(size)
z = np.ones(size)
u = np.ones(size)


for i in range(len(dist)):
    plotx[i] = i+1
    i+1

    #Method 1
for i in range(len(dist)-1):
    x[i] = np.random.uniform()
    x[i+1] = np.random.uniform()
    # print(x)

    y[i] = sqrt(-2*np.log(x[i]))*np.cos(2*pi*x[i+1])
    y[i] = sqrt(-2*np.log(x[i]))*np.sin(2*pi*x[i+1])

    z[i] = mean + sigma*y[i]
    z[i+1] = mean + sigma*y[i+1]
    dist[i] = z[i]
    dist[i+1] = z[i+1]
    i = i+1
# print(dist)




# Method 2

#written as function to use in notebook
def RandomGen(size, mean, sigma):
    dist = np.ones(size)
    dist2 = np.ones(size)

    plotx = np.ones(size)
    x = np.ones(size)
    y = np.ones(size)
    z = np.ones(size)
    u = np.ones(size)


    for i in range(len(dist)):
        plotx[i] = i+1
        i+1

    i = 0
    for i in range(len(dist)-1):
        x[i] = np.random.uniform()
        x[i+1] = np.random.uniform()

        u[i] = (2*x[i]) - 1
        u[i+1] = (2*x[i+1]) - 1
        d = u[i]**2 - u[i+1]**2
        # print('FIRST D', d)
        while d < 1e-2 or d > 1:
            x[i] = np.random.uniform()
            x[i+1] = np.random.uniform()

            u[i] = (2*x[i]) - 1
            u[i+1] = (2*x[i+1]) - 1
            d = u[i]**2 - u[i+1]**2
            # print('D VALUE:', d)

        y[i] = u[i]*sqrt((-2*np.log(d))/d)
        y[i+1] = u[i+1]*sqrt((-2*np.log(d))/d)
        # print(y[i])
        z[i] = mean + sigma*y[i]
        z[i+1] = mean + sigma*y[i+1]
    return z

#Un-comment to show in terminal
# print(z)
# print(np.mean(z), np.max(z), np.min(z))
# print(z)
# plt.plot(plotx, z)
# plt.plot(plotx, y)
# plt.hist(z, 200)
# plt.xlim([-100, 100])
# plt.show()
