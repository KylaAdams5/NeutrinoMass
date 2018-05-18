'''
Kyla Adams

Last Modified 28/03/18

Code generate a least squares fit to given data
'''

# Import all the necessary Packages for this script
import numpy as np
from math import *
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from scipy.optimize import lsq_linear
import ipywidgets as widgets

# Import the pre-written code to import the data
from import_data import importData

# Import the csv file and set up the variable names using prewritten function
data, current, currentErr, counts, countCorr, B, BErr, p, E_totJ, E_totkeV, T, KurieVar, r, rErr = importData('data_b_headers.csv')
KineticE = E_totkeV - 511

# Function to display the code if desired
def data_show(show=False):
    if show:
        print(data)
data_show()

# The data is imported as a Pandas array to make viewing easier in ipython
# better to translate into numpy array to do data manipulation

# Convert to numpy array
x = pd.DataFrame.as_matrix(KineticE)
y =  pd.DataFrame.as_matrix(KurieVar)
x = np.ravel(x)
y = np.ravel(y)

# Take the linear part of the data as decided in 'KuriePlot.py'
x = x[3:7]
y = y[3:7]

# Define linear fit to check my regression
def linear(x, m, c):
    return  (m*x) + c

# Predefined function to check regression values are ok
poptdata1, pcovdata1 = curve_fit(linear, x, y, p0 = [1e20, 3e23],xtol = 1e-15, ftol = 1e-15, gtol = 1e-15, verbose = 0, method = 'trf')
perr1 = np.sqrt(np.diag(pcovdata1))
# print(poptdata1, pcovdata1, perr1)

# Define variables to store the sum of the x and y arrays
sum_x = 0
sum_y = 0

# Find the sum of the arrays
for i in range(len(x)):
    sum_x = sum_x + x[i]
    sum_y = sum_y + y[i]
# print('sum', sum_x, sum(x))

#Find the mean using the predefined function len()
mean_x = sum_x/len(x)
mean_y = sum_y/len(y)

# Define blank arrays to find the gradient from the data
num = 0
denom = 0
for i in range(len(x)):
    num = num + (x[i] - mean_x)*(y[i] - mean_y)
    denom = denom + (x[i] - mean_x)**2
    m = num/denom
# print('gradient', m)

# Find the y-intercept from calculated gradient
c = mean_y - (m*mean_x)
# print('intercept', c)

# Find the error in the values using the deviation from the actual data
# Need to add the data errors to these and have a max dara error and min
Error = 0
for i in range(len(x)):
    Error = Error + (2*(y[i] - (m*x[i] + c))*(-x[i]))
# print('Error', abs(Error))
ErrArray = [abs(Error)] * 4
# print('Error', ErrArray)

# Find the variance in the data
xvariance = 0
yvariance = 0
for i in range(len(x)):
    xvariance = xvariance +  (x[i] - mean_x)**2
    yvariance = yvariance +  (y[i] - mean_y)**2

xvariance = sqrt((1/len(x) * xvariance))
yvariance = sqrt((1/len(y) * yvariance))

# print('Variance is', xvariance, yvariance)

xErrArray = [xvariance, xvariance, xvariance, xvariance]
yErrArray = [yvariance, yvariance, yvariance, yvariance]

def plot(fitshow=True, linfit=True, Errorbar=True):
    '''Plots the calculated data with the linear fit and error bars if desired'''
    plt.plot(x,y, label = 'data')

    if linfit:
        # Plot the data with the linear fit
        print('Plotting the least squares fit...')
        plt.plot(x, linear(x, m, c), label = 'fit')
        # plt.yscale('log')

    if Errorbar:
        print('Plotting the calculated 1 sigma variance...')
        plt.errorbar(x, linear(x,m,c), yErrArray, xErrArray, ecolor = 'lightgrey', color = 'o', ls = '', label = '1 STD error')

    plt.xlabel('Kinetic Energy keV')
    plt.ylabel('KurieVar')
    plt.title('Kurie Plot')
    plt.legend()
    plt.show()

def slider():
    w = widgets.IntSlider(
    value=7,
    min=-3,
    max=10,
    step=1,
    description='My patience level:',
    disabled=False,
    continuous_update=True,
    orientation='horizontal',
    readout=True,
    readout_format='d'
        )
    return(w)
