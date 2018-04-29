'''
Kyla Adams

Last Modified 21/3/18 5:15pm

Code generate a Kurie plot from the data set as imported from import_data.py
'''

import numpy as np
import matplotlib.pyplot as plt

from import_data import importData

# Import the csv file and set up the variable names using prewritten function
data, current, currentErr, counts, countCorr, B, BErr, p, E_totJ, E_totkeV, T, KurieVar, r, rErr = importData('data_b_headers.csv')


KineticE = E_totkeV - 511
print(KineticE)
#Plot the Kurie variable against the energy and show the linear region
plt.figure()
# plt.plot(E_totkeV, KurieVar)
plt.plot(KineticE, KurieVar)

# plt.axvline(100, color = 'r')
# plt.axvline(190, color = 'r')
plt.xlabel('Kinetic Energy (keV)')
plt.ylabel('Kurie Variable')
plt.ylim([1e21,1e23])
# plt.yscale('log')
# plt.xlim([500, 800])
plt.title('Kurie Variable Evolution')
plt.show()

# Just plot the linear region
plt.figure()
plt.plot(KineticE, KurieVar)
plt.xlabel('Kinteic Energy (keV)')
plt.ylabel('Kurie Variable')
plt.ylim([1e21,0.9e23])
# plt.yscale('log')
plt.xlim([100, 190])
plt.title('Kurie Plot')
plt.show()
