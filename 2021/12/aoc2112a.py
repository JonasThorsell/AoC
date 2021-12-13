<<<<<<< HEAD
# Copyright (c) 2021 Jonas Thorsell
import sys
from collections import defaultdict

def trace(r,m,v):
    if r == 'end':
        return 1
    if r[0].islower():
        if r in v:
            return 0
        v.add(r)
    s = 0
    for p in m[r]:
        s += trace(p,m,v.copy())
    return s

m = defaultdict(set)
for l in sys.stdin:
    a,b = l.strip().split('-')
    m[a].add(b)
    m[b].add(a)
print(trace('start',m,set()))
=======
# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

g = []
for l in sys.stdin:
    g.append([int(c) for c in l.strip()])
g = np.array(g)
f=0
for n in range(100):
    g += 1
    while np.count_nonzero(g > 9):
        p = np.where(g > 9)
        x,y = p[0][0], p[1][0]
        w,h = g.shape
        if x>0 and y>0 and g[x-1,y-1]>0: g[x-1,y-1] += 1
        if x>0 and g[x-1,y]>0: g[x-1,y] += 1
        if x>0 and y+1<h and g[x-1,y+1]>0: g[x-1,y+1] += 1
        if y>0 and g[x,y-1]>0: g[x,y-1] += 1
        if y+1<h and g[x,y+1]>0: g[x,y+1] += 1
        if x+1<w and y>0 and g[x+1,y-1]>0: g[x+1,y-1] += 1
        if x+1<w and g[x+1,y]>0: g[x+1,y] += 1
        if x+1<w and y+1<h and g[x+1,y+1]>0: g[x+1,y+1] += 1
        g[x,y] = 0
        f += 1

print(f)
>>>>>>> a45011f3ecd5d7d1bb285bc0c66b7b37e187a185
