# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

g = np.zeros((1000,1000))
for l in sys.stdin:
    w = l.strip().split()
    o = 1 if w[0] == 'toggle' else 2
    x0,y0 = [int(i) for i in w[o].split(',')]
    x1,y1 = [int(i)+1 for i in w[o+2].split(',')]
    if w[1] == 'on':
        g[x0:x1,y0:y1] = g[x0:x1,y0:y1]+1
    elif w[1] == 'off':
        g[x0:x1,y0:y1] = np.clip(g[x0:x1,y0:y1]-1, 0, None)
    else:
        g[x0:x1,y0:y1] = g[x0:x1,y0:y1]+2
print(int(np.sum(g)))
