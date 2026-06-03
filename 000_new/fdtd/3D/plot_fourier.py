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
import image
# import imageChops
# from mayavi import mlab

# four = open('ampl.dat','r')
amp = np.loadtxt('ampl.dat', delimiter = '\n')
amp = amp[~np.isnan(amp)]

fig = plt.figure()
ax = plt.axes()
ax.plot(amp,'o')
plt.show()