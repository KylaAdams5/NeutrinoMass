'''
Code to simulate a Neutrino Beam

Kyla Adams

'''

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from math import *
from RandomDist import RandomGen

m_pion = 0.1396 #GeV/c^2
m_kaon = 0.4937 #GeV/c^2
m_muon = 0.1057 # GeV/c^2
tau_pion = 2.608*1e-8 #s
tau_kaon = 1.237*1e-8 #s
t_pion = -tau_pion * np.log(np.random.uniform(0, 1, 860))
t_kaon = -tau_kaon * np.log(np.random.uniform(0, 1, 140))

c = 2.9*1e8 #m/s adjust for units

# Randomly generate the disributions for both the pions and kaons
MomentaDistributionPion = RandomGen(860, 200, 10)
MomentaDistributionKaon = RandomGen(140, 200, 10)

# set as array to make easier to call in notebook
MomentaDistribution = (MomentaDistributionPion, MomentaDistributionKaon)

# Calculate the decay distance of the mesons
distancePion = (MomentaDistributionPion/m_pion) * c * t_pion
distanceKaon = (MomentaDistributionKaon/m_kaon) * c * t_kaon

# again set as array to make life easier
distance = [distancePion, distanceKaon]

#Check values
print('Pion Dist', np.mean(MomentaDistributionPion), '\n Kaon Dist', np.mean(MomentaDistributionKaon))

print('Pion distance', np.mean(distancePion), '\n Kaon distance', np.mean(distanceKaon))


# Calculate the decay distances of the neutrinos
#longitudinal momentum
pRestPion = (m_pion**2 - m_muon**2)/(2*m_pion)
pRestKaon = (m_kaon**2 - m_muon**2)/(2*m_kaon)
print('rest', pRestKaon, pRestPion)
theta = np.random.uniform(-1, 1, 860)

plPion = np.abs(pRestPion)*np.cos(theta)
ptPion = np.abs(pRestPion)*np.sin(theta)

plKaon = np.abs(pRestKaon)*np.cos(theta)
ptKaon = np.abs(pRestKaon)*np.sin(theta)

longitudeMomenta = [plPion, plKaon]
transverseMomenta = [ptPion, ptKaon]

betaPion = np.abs(MomentaDistributionPion)/(np.sqrt(MomentaDistributionPion**2 + m_pion**2))
betaKaon = np.abs(MomentaDistributionKaon)/(np.sqrt(MomentaDistributionKaon**2 + m_kaon**2))

gammaPion = 1/(np.sqrt(1-betaPion**2))
gammaKaon = 1/(np.sqrt(1-betaKaon**2))

E = np.abs(MomentaDistributionPion)
betagammaPion = betaPion*gammaPion
a = np.array([[gammaPion, 0, betagammaPion], [0,1,0], [betagammaPion, 0, gammaPion]])
b = np.array([[plPion], [ptPion], [np.abs(MomentaDistributionPion)]])
cMx = [(gammaPion*plPion + betagammaPion*E), (ptPion), ((betagammaPion*plPion)+ (gammaPion*E))]


sinthetaLab = np.abs(cMx[1])/cMx[2]
print(sinthetaLab[0:10])
print(ptPion[0:10])

detect = 0
r = distancePion
for i in range(len(distancePion)):
    test = np.abs((distancePion[i] - 700))*(sinthetaLab[i])
    if test <= 1.5:
        detect = detect + 1
        r[i] = test

print(detect, r[0:10])
r = np.abs((distancePion - 700))*(sinthetaLab)
plt.figure()
plt.hist(r, bins = 100)
plt.show()

################################
######## Functions #############

def plothist(dat, pion=True, kaon=False, Title = 'Momenta Distributions', binsize = 20, label = 'Momenta (GeV/c^2)'):
    '''Function to show histograms in the notebook '''
    if pion:
        print('Plotting the momenta distribution of decaying pions...')
        Title = Title + 'of Pions'
        plt.hist(dat[0], alpha = 0.4, bins = binsize, label='Pions')
    if kaon:
        print('Plotting the momenta distribution of decaying kaons...')
        Title = Title + ' of Kaons'
        plt.hist(dat[1], alpha = 0.4, bins = binsize, label='Kaons')
    plt.title(Title)
    plt.xlabel(label)
    plt.legend()
    plt.show()


# beta = np.abs(MomentaDistribution)/np.sqrt(MomentaDistribution**2 + m_pion**2)

#Function to import data into notebook
def outputDistributions():
    return (MomentaDistribution, distance)

def outputMomenta():
    return (longitudeMomenta, transverseMomenta)

# Code to plot when just using the terminal
plt.figure()
plt.hist(distancePion/1e20, 20, label = 'Pion')
plt.hist(distanceKaon, 20, label = 'Kaon')
plt.legend()
# plt.show()
