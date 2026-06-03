#!/usr/bin/python

from pylab import *

import ltspy

sd=ltspy.SimData('tb_pulsels.raw')

nvout = sd.variables.index('V(out)')
ntime = 0

for nrun in range(sd.nosteps):
    plot(sd.values[ntime][nrun],sd.values[nvout][nrun])
show()
