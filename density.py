import scipy.integrate as integrate
from math import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors, ticker, cm

#Initiailise variables needed and arrays
g = 4
T = 3 #ev
n = 410
k_b = 1.38e-23
h_bar = 1.0553e-34
c = 3e8
G = 6.67e-11

T = np.logspace(-3,2, num = 200)
x = np.zeros(200)
err = np.zeros(200)
f = lambda p: g/(2*pi**2)*(1/(np.expm1(p/T[i])))*p**2

#Integration frunction for the relative neutrino density
for i in range(len(T)):
    test,err2 = integrate.quad(f, 0, np.inf)
    x[i] = test
    err[i] = err2

r = x/n

def plotdensity():
    plt.figure()
    plt.yscale('linear')
    plt.xscale('linear')
    plt.plot(T,r)
    plt.xlabel('Temperature')
    plt.ylabel('relative number density of neutrinos as equilibrium')
    plt.show()

#Initialise more arrays for the next function
m = np.linspace(0.0001, 1, 200)
rnu = np.zeros((200,200))

for i in range(len(m)):
    for j in range(len(r)):
        beta = 0.29 * m[i]**2
        func = lambda rnu: -beta*(rnu**2 - r[j]**2)
        rnu[i,j], err = integrate.quad(func, 0, 500)

def plotMassTemp():
    plt.figure()
    plt.plot(r,rnu)
    plt.xlabel('Neutrino Equilibrium density ')
    plt.ylabel('Neutrino Density (MeV/c^2)')
    plt.yscale('log')
    plt.xscale('log')
    plt.show()
# plotMassTemp()

###############
# Extra section on Friedman integration - not mentioned in pdf or notebook
const = np.sqrt((8*pi**3*G*k_b**4)/(45*c**7*h_bar**3))
t = np.linspace(1, 10000, 200)
a = lambda T: T**2*const*t[i]**-0.5
friedman = np.zeros(200)
for i in range(len(T)):
    friedman2, err = integrate.quad(a, 0, np.inf)
    friedman[i] = friedman2

def plotFriedman():
    plt.figure()
    plt.plot(t,friedman)
    plt.yscale('log')
    plt.xlabel('Time')
    plt.ylabel('')
    plt.show()

# plotFriedman()
