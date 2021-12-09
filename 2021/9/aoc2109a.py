# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

hm = []
for l in sys.stdin:
    hm.append([int(x) for x in l.strip()])
hm = np.pad(np.array(hm),1,'maximum')
lmm = (hm < np.roll(hm, 1, 0)) & \
      (hm < np.roll(hm,-1, 0)) & \
      (hm < np.roll(hm, 1, 1)) & \
      (hm < np.roll(hm,-1, 1))
print(sum(hm[lmm]+1))
