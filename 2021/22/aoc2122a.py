# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

rc = np.zeros((101,101,101),dtype=np.uint)
for l in sys.stdin:
    cmd, cords=l.split()
    c = [[int(y)+50 for y in x[2:].split('..')] for x in cords.split(',')]
    if c[0][0] > 100 or c[0][1] < 0 or c[1][0] > 100 or c[1][1] < 0 or c[2][0] > 100 or c[2][1] < 0:
        continue
    rc[max(c[0][0],0):min(c[0][1],100)+1, max(c[1][0],0):min(c[1][1],100)+1, max(c[2][0],0):min(c[2][1],100)+1] = 1 if cmd=='on' else 0

print(np.sum(rc))
