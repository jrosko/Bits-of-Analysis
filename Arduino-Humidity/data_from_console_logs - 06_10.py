import re
import matplotlib.pyplot as plt
from itertools import cycle

re_hum='ity: \d\d\.\d\d %'
re_temp='emp: \d\d\.\d\d C'
re_time='\d\d:\d\d:\d\d\.\d\d\d'

paths = [r'C:\Users\elpresidente_2\Documents\GitHub\Bits-of-Analysis\Arduino-Humidity\ard_humidity_eppens_06_10.txt']

data=[]

for path in paths:
    print(path)
    data_part=[]
    with open(path,'r', encoding='utf8') as f:
        for line in f.readlines():
            time = re.search(re_time,line)
            print(time)
            if type(time)!=None:
                time = time.group()
                hum = re.search(re_hum,line)
                hum = float(hum.group()[5:10])
                temp = re.search(re_temp,line)
                temp = float(temp.group()[5:10])
                data_part.append([time, temp, hum])
    f.close()
    data.append(data_part)

fig, ax = plt.subplots(1,1, figsize=(4.3,3),sharex=True, dpi=600)

def stamp2sec(stamp):
    hours = stamp[0:2]
    minutes = stamp[3:5]
    seconds = stamp[6:8]
    return float(int(hours)*60 + int(minutes) + int(seconds)/60)



k=0
for condition in data:
    time = [stamp2sec(item[0])-stamp2sec(condition[0][0]) for item in condition]
    temp = [item[1] for item in condition]
    hum = [item[2] for item in condition]
    ax.plot(time, temp, '.', color='red')
    ax.set_ylim(20,39)
    if k!=0:
        ax.set_xlabel('Time (min)')
    k=k+1
    ax.tick_params(axis='y', labelcolor='red')
    ax.set_ylabel('Temp. (C)',color='red')
    ax_ = ax.twinx()
    ax_.set_ylim(20,70)
    ax_.plot(time, hum, '.',color='navy' )
    ax_.tick_params(axis='y', labelcolor='navy')
    ax_.set_ylabel('Rel. Humid. (%)',color='navy')

plt.subplots_adjust(left=0.15, right=0.85, bottom=0.15 )



plt.savefig('figure-06_10.png')
