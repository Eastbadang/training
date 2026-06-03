import numpy as np
from numpy import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import sys
import os
import subprocess
import Image
import ImageChops

datafile = "data_patch_antenna.dat"
datafile = "data.dat"
print ("Importing data from " + datafile + "...")
print ("Using comma delimiter")

f = open(datafile,'r')
header = f.readline()
header = header.strip().split("\t")
NX = int(header[0])
NY = int(header[1])
NZ = int(header[2])
T = int(header[3])-1

uu = zeros([T,NX,NY,NZ])
for n in range(T):
	for k in range(NZ):
		for j in range(NY):
			for i in range(NX): 
				uu[n,i,j,k] = f.readline().strip()

print ("Domain size: " + str(size(uu)))
# uu = uu.reshape(T,NX,NY)
set_printoptions(threshold=nan)
# print shape(uu)
# uu = uu.reshape(T,NZ,NY,NX)
# uu = np.swapaxes(uu,1,3)
f.close()

v = sum(uu[:,22,14,0:2],axis=-1)
vfft = np.fft.fft(v)
freqs = np.fft.fftfreq(T,d=1.667e-11)

# fig1 = plt.figure()
# ax1 = plt.axes(xlim=[0,max(freqs)*1.2],ylim=[1.2*min(v),1.2*max(v)])
# ax1.plot(v)

# fig2 = plt.figure()
# ax2 = plt.axes()
plt.plot(freqs[1:T/2],np.abs(vfft)[1:T/2])
plt.show()

