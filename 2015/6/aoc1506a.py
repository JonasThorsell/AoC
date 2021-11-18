# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

g = np.full((1000,1000), False)
for l in sys.stdin:
    w = l.strip().split()
    o = 1 if w[0] == 'toggle' else 2
    x0,y0 = [int(i) for i in w[o].split(',')]
    x1,y1 = [int(i)+1 for i in w[o+2].split(',')]
    if w[1] == 'on':
        g[x0:x1,y0:y1] = True
    elif w[1] == 'off':
        g[x0:x1,y0:y1] = False
    else:
        g[x0:x1,y0:y1] = ~g[x0:x1,y0:y1]
print(np.count_nonzero(g))
