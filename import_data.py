'''
Kyla Adams

Last Modified 20/3/18 9:40am

Code to import the data file and convert to arrays using pandas
'''

import pandas as pd

def importData(dat):

#### Set up the data to make plots and fits ###
    data = pd.read_csv('/Users/kylaadams/UniMelbCourse/Computing/data_files/'+dat, sep = ',', header = 1, skipfooter = 11, engine = 'python', skip_blank_lines = 'True')
    # Create the counts array
    current = data.loc[:, ['Current']]

    #Create the count error array
    currentErr = data.loc[:, ['SystUncert']]

    counts = data.loc[:, ['Counts']]
    countCorr = data.loc[:, ['Corrected counts']]

    B = data.loc[:, ['B']]
    BErr =  data.loc[:, ['SystUncertB']]
    p =  data.loc[:, ['p']]
    E_totkeV =  data.loc[:, ['E_tot_KeV']]
    E_totJ = data.loc[:,['E_tot_J']]
    T =  data.loc[:, ['T']]
    KurieVar =  data.loc[:, ['Kurie Variable']]
    r = 3.80
    rErr = 0.01

    return(data, current, currentErr, counts, countCorr, B, BErr, p, E_totJ, E_totkeV, T, KurieVar, r, rErr)

# data, current, currentErr, counts, countCorr, B, BErr, p, E_totJ, E_totkeV, T, KurieVar = importData('data_b_headers.csv')
# print(data)
