import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import pims
import trackpy as tp
import cv2


path = r'C:\Users\elpresidente_2\Desktop\MatlabPA14\Particle Tracking\cropped_movie'
frames = pims.open(path + r'\*.tif')
print(type(frames))
proc_frames = []
# First detect particles in each frame
for frame in frames:
    frame_ = cv2.GaussianBlur(frame,(5,5),0)
    frame = cv2.adaptiveThreshold(frame_,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,2)
    proc_frames.append(frame)


loc = tp.batch(proc_frames, 13, invert=True, minmass=2000) # Found minmass from histogram

t = tp.link(loc, 9, memory = 4)
t1 = tp.filter_stubs(t, 20)
plt.figure()
tp.plot_traj(t1)
plt.show()



#tp.annotate(f, frames[0])



#fig, ax = plt.subplots()
#ax.hist(f['mass'], bins=20)
#ax.set_xlabel('mass')
#ax.set_ylabel('count')
#plt.show()

#f = tp.locate(th3, 13, invert=True, minmass = 2000)
#tp.annotate(f, frame)

##plt.imshow(frames[0])
#plt.show()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
