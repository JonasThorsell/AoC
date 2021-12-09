# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

def fmin(x,y,hm):
    if hm[x,y] > 8: return 0
    m = set()
    if (hm[x+1,y]<hm[x,y]): m.add(fmin(x+1,y,hm))
    if (hm[x-1,y]<hm[x,y]): m.add(fmin(x-1,y,hm))
    if (hm[x,y+1]<hm[x,y]): m.add(fmin(x,y+1,hm))
    if (hm[x,y-1]<hm[x,y]): m.add(fmin(x,y-1,hm))
    m = list(filter(None, m))
    if len(m) == 1:
        return m[0]
    if len(m) == 0:
        return y*10000+x*10+1
    return 0

hm = []
for l in sys.stdin:
    hm.append([int(x) for x in l.strip()])
hm = np.pad(np.array(hm),1,'maximum')

bm = np.empty(hm.shape)
for x,y in np.ndindex(hm.shape):
    bm[x,y] = fmin(x,y,hm)

bs = sorted([(bm==n).sum() for n in np.unique(bm) if n != 0], reverse=True)
print(np.prod(bs[:3]))
