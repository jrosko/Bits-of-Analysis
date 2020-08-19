"""
OD and clumping analysis
"""
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle


fig, ax = plt.subplots(figsize=(4,3), dpi=900)
data = {}

# Load the 17.08.2020 Data
data_ = np.genfromtxt('D:\Little Bits of Analysis\OD and Clumping\Data_17_08_2020.txt')
data['PBS_17_08'] = [data_[:,0],  data_[:,1]]
data['PBS_Trit_17_08'] = [data_[:,0],  data_[:,2]]
# Load the 02.07.2020 Data
data_ = np.genfromtxt('D:\Little Bits of Analysis\OD and Clumping\Data_02_07_2020.txt')
data['PBS_02_07']= [data_[:,0], data_[:,1]]

colors = cycle(['red', 'blue', 'orange'])
keys = cycle(data.keys())

for key in data:
    print(data[key])
    ax.plot(data[key][0], data[key][1],'o', color = next(colors), label = next(keys))

ax.legend(fontsize=10,handlelength=0.2, borderpad=0.5, handletextpad=0.6)
fontsize = 12

ax.set_ylabel('OD600', fontsize = fontsize)
ax.set_xlabel('Time [min]',  fontsize = fontsize)
ax.set_title('OD600 as f(time) since first measurement',  fontsize = 10)

plt.subplots_adjust(left=0.18, bottom=0.15 )
plt.savefig('figure.png')
