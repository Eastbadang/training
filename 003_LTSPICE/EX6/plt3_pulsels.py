#!/usr/bin/python3

from pylab import *

import ltspy3

sd=ltspy3.SimData('tb_pulsels.raw')

nvout = sd.variables.index(b'V(out)')
ntime = 0

for nrun in range(sd.nosteps):
    plot(sd.values[ntime][nrun],sd.values[nvout][nrun])
show()
