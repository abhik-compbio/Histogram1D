# Pyhton code to compare dihedral angle distribution of two different trajectory
# Made by Abhik Ghosh Moulick, SNBNCBS

import numpy as np
import math
import matplotlib.pyplot as plt
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
maxbin = 45   # Maximum number of bin
binwidth = 180/45  # Binwidth
xlist = np.linspace(-180, 180, 91)

# at ph7  
n1 = 20000
hisph1 = np.zeros([2*maxbin+1])
hisps1 = np.zeros([2*maxbin+1])
phi1 = np.zeros(n1)
psi1 = np.zeros(n1)
f1 = open('dihed-res1-ph7.dat','r')

# at ph1
n2 = 20000
hisph2 = np.zeros([2*maxbin+1])
hisps2 = np.zeros([2*maxbin+1])
phi2 = np.zeros(n2)
psi2 = np.zeros(n2)
f2 = open('dihed-res1-ph1.dat','r')


# ph7 analysis
for i in range(n1):
	s = f1.readline()
	token = s.split()
	#junk1 = token[0]
	#junk2 = token[1]
	phi1[i] = token[0]
	psi1[i] = token[1]
	if (phi1[i] > 180.0000):
		phi1[i] = phi1[i]-360.0000
	if (phi1[i] < -180.0000):
		phi1[i] = phi1[i]+360.0000
	if (psi1[i] > 180.0000):
		psi1[i] = psi1[i]-360.0000
	if (psi1[i] < -180.0000):
		psi1[i] = psi1[i]+360.0000
	a1 = phi1[i] + 180
	a2 = psi1[i] + 180
	if (a1 % binwidth == 0.0):
		l1 = int(a1/binwidth)
	else: 
		l1 = int(a1/binwidth) + int(1)
	if (a2 % binwidth == 0.0):
		l2 = int(a2/binwidth)
	else: 
		l2 = int(a2/binwidth) + int(1)
	hisph1[l1] = hisph1[l1] + int(1)
	hisps1[l2] = hisps1[l2] + int(1)

# PH 7 HISTOGRAM FILE	
hisph1 = hisph1/int(n1)   
hisps1 = hisps1/int(n1)

# ph1 analysis
for i in range(n2):
	s = f2.readline()
	token = s.split()
	#junk1 = token[0]
	#junk2 = token[1]
	phi2[i] = token[0]
	psi2[i] = token[1]
	if (phi2[i] > 180.0000):
		phi2[i] = phi2[i]-360.0000
	if (phi2[i] < -180.0000):
		phi2[i] = phi2[i]+360.0000
	if (psi2[i] > 180.0000):
		psi2[i] = psi2[i]-360.0000
	if (psi2[i] < -180.0000):
		psi2[i] = psi2[i]+360.0000
	a1 = phi2[i] + 180
	a2 = psi2[i] + 180
	if (a1 % binwidth == 0.0):
		l1 = int(a1/binwidth)
	else: 
		l1 = int(a1/binwidth) + int(1)
	if (a2 % binwidth == 0.0):
		l2 = int(a2/binwidth)
	else: 
		l2 = int(a2/binwidth) + int(1)
	hisph2[l1] = hisph2[l1] + int(1)
	hisps2[l2] = hisps2[l2] + int(1)

# PH 1 HISTOGRAM FILE
	
hisph2 = hisph2/int(n2)
hisps2 = hisps2/int(n2)

plt.figure(1)
plt.figure(figsize=(8,6))
plt.xlabel('Angle',fontdict=font)
plt.ylabel('Hist(Angle)',fontdict=font)
plt.title('Residue1 Dihedral $\phi$/$\psi$ distribution',fontdict=font)
plt.plot(xlist,hisph1,linestyle='-',marker='o',label='ph7-$\phi$',color='b')
plt.plot(xlist,hisph2,linestyle='-',marker='o',label='ph1-$\phi$',color='g')
plt.plot(xlist,hisps1,linestyle='-',marker='o',label='ph7-$\psi$',color='r')
plt.plot(xlist,hisps2,linestyle='-',marker='o',label='ph1-$\psi$',color='k')
plt.legend()
plt.xlim(-180,180)
plt.savefig('dist-Residue1')

	

