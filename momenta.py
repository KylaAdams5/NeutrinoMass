'''
Code to simulate a Neutrino Beam

Kyla Adams

Main steps outlined in both notebook and accompnaying report

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
c = 2.9e8 #m/s

initialpion = 86000 # percentage of beam pions
initialkaon = 14000 # percentage of beam Kaons
mean = 200
std = 10
# calculated the lab frame time
t_pion = -tau_pion * np.log(np.random.uniform(0, 1, initialpion))
t_kaon = -tau_kaon * np.log(np.random.uniform(0, 1, initialkaon))


# Randomly generate the disributions for both the pions and kaons
MomentaDistributionPion = RandomGen(initialpion, mean, std)
MomentaDistributionKaon = RandomGen(initialkaon, mean, std)

# set as array to make easier to call in notebook
MomentaDistribution = (MomentaDistributionPion, MomentaDistributionKaon)

# calculate the relevant components for Lorentz Transformation
betaPion = np.abs(MomentaDistributionPion)/(np.sqrt(MomentaDistributionPion**2 + m_pion**2))
betaKaon = np.abs(MomentaDistributionKaon)/(np.sqrt(MomentaDistributionKaon**2 + m_kaon**2))

gammaPion = 1/(np.sqrt(1-betaPion**2))
gammaKaon = 1/(np.sqrt(1-betaKaon**2))

betagammaPion = betaPion*gammaPion
betagammaKaon = betaKaon*gammaKaon

Epion = np.abs(MomentaDistributionPion)
Ekaon = np.abs(MomentaDistributionKaon)

# Calculate the decay distances of the neutrinos

pRestPion = (m_pion**2 - m_muon**2)/(2*m_pion)
pRestKaon = (m_kaon**2 - m_muon**2)/(2*m_kaon)

#print('rest', pRestKaon, pRestPion) #un-comment to print in terminal
thetaPion = np.random.uniform(-1, 1, initialpion)
thetaKaon = np.random.uniform(-1, 1, initialkaon)

#longitudinal and transverse pion momenta
plPion = np.abs(pRestPion)*np.cos(thetaPion)
ptPion = np.abs(pRestPion)*np.sin(thetaPion)

#longitudinal and transverse pion momenta
plKaon = np.abs(pRestKaon)*np.cos(thetaKaon)
ptKaon = np.abs(pRestKaon)*np.sin(thetaKaon)

#store as arrays to call in notebook
longitudeMomenta = [plPion, plKaon]
transverseMomenta = [ptPion, ptKaon]

# Calculate the matrix elements of the transform
aPion = np.array([[gammaPion, 0, betagammaPion], [0,1,0], [betagammaPion, 0, gammaPion]])
aKaon = np.array([[gammaKaon, 0, betagammaKaon], [0,1,0], [betagammaKaon, 0, gammaKaon]])

bPion = np.array([[plPion], [ptPion], [np.abs(MomentaDistributionPion)]])
bKaon = np.array([[plKaon], [ptKaon], [np.abs(MomentaDistributionKaon)]])

cMxPion = [(gammaPion*plPion + betagammaPion*Epion), (ptPion), ((betagammaPion*plPion)+ (gammaPion*Epion))]
cMxKaon = [(gammaKaon*plKaon + betagammaKaon*Ekaon), (ptKaon), ((betagammaKaon*plKaon)+ (gammaKaon*Ekaon))]

# Calculate the decay distance of the mesons
# distancePion = (MomentaDistributionPion/m_pion) * t_pion * c
# distanceKaon = (MomentaDistributionKaon/m_kaon) * t_kaon * c

distancePion = (cMxPion[0]/m_pion) * t_pion * c
distanceKaon = (cMxKaon[0]/m_kaon) * t_kaon * c

# again set as array to make life easier
distance = [distancePion, distanceKaon]

#Check values (un-comment for terminal use)
# print('Pion Dist', np.mean(MomentaDistributionPion), '\n Kaon Dist', np.mean(MomentaDistributionKaon))

# print('Pion distance', np.mean(distancePion), '\n Kaon distance', np.mean(distanceKaon))

# Determine whether the neutrino hits the detector plate

sinthetaLabPion = np.abs(cMxPion[1])/cMxPion[2]
sinthetaLabKaon = np.abs(cMxKaon[1])/cMxKaon[2]

detectPion = 0
detectKaon = 0
transverseP = cMxPion[1]
transverseK = cMxKaon[1]
rpion = cMxPion[1]
rkaon = cMxKaon[1]

for i in range(len(transverseK)):
    test = np.abs((transverseK[i] - 700))*(sinthetaLabKaon[i])
    if test <= 1.5:
        detectKaon = detectKaon + 1
        rkaon[i] = test

for i in range(len(transverseP)):
    test = np.abs((transverseP[i] - 700))*(sinthetaLabPion[i])
    if test < 1.5:
        detectPion = detectPion + 1
        rpion[i] = test

def percentagedetect(pion= True, kaon=False):
    if pion:
        percentpion = detectPion/initialpion
        print('Percentage Detected ', percentpion*100, '%')
    if kaon:
        percentkaon = detectKaon/initialkaon
        print('Percentage Detected ', percentkaon*100, '%')

# print("No. Detections kaon", detectKaon)
# print("No. Detections Pion", detectPion)

rK = np.abs((transverseK - 700))*(sinthetaLabKaon)
rP = np.abs((transverseK - 700))*(sinthetaLabKaon)
r = [rP, rK]

################################
######## Functions #############

def plothist(dat, pion=True, kaon=False, Title = 'Momenta Distributions ', binsize = 20, label = 'Momenta (GeV/c^2)'):
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

#Function to import data into notebook
def outputDistributions():
    return (MomentaDistribution, distance)

def outputMomenta():
    return (longitudeMomenta, transverseMomenta)

def outputRadius():
    return r

# Code to plot when just using the terminal
# plt.figure()
# plt.hist(distancePion/1e20, 20, label = 'Pion')
# plt.hist(distanceKaon, 20, label = 'Kaon')
# plt.legend()
# plt.show()
