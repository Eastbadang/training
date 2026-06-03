# pip install ltspice
# pip install matplotlib

import ltspice
import matplotlib.pyplot as plt
import numpy as np
import os


filepath = 'rc.raw'

l = ltspice.Ltspice(filepath)
#l = ltspice.Ltspice(os.path.dirname(__file__)+'\\rc.raw')

# Make sure that the .raw file is located in the correct path
l.parse() # Data loading sequence. It may take few minutes.

time = l.get_time()
V_source = l.get_data('V(source)')
V_cap = l.get_data('V(cap)')

plt.plot(time, V_source)
plt.plot(time, V_cap)
plt.show()