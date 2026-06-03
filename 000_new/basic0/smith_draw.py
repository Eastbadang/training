# pip install scikit-rf

import matplotlib.pyplot as plt
import skrf as rf


ntwk=rf.Network('preamp_b.s2p')
#ntwk.plot_s_smith()
#ntwk.plot_s_smith(draw_labels=True)
ntwk.plot_s_db()
#print(ntwk)

#plt.figure()
plt.title('Measured data')
plt.xlabel('Frequency[Hz]')
plt.ylabel('S parameter[dB]')
plt.show()







