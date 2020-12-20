# Copyright (c) 2020 Jonas Thorsell
import sys
import numpy as np

tb = {}
ti = {}
for l in sys.stdin:
    if l.strip():
        i = int(l.strip()[5:-1])
        d = []
        for l in sys.stdin:
            if not l.strip():
                break
            d.append(['1' if x == '#' else '0' for x in l.strip()])
        ti[i] = np.array(d)
        tb[i] = ( "".join(ti[i][ 0, :]), \
                  "".join(ti[i][ :,-1]), \
                  "".join(np.flipud(ti[i][-1, :])), \
                  "".join(np.flipud(ti[i][ :, 0])), \
                  "".join(np.flipud(ti[i][ 0, :])), \
                  "".join(ti[i][ :,0]), \
                  "".join(ti[i][-1, :]), \
                  "".join(np.flipud(ti[i][ :, -1])) )

def cnt(tb, i):
    c = 0
    for k in tb:
        if k == i:
            continue
        for j in range(4):
            if (tb[i][j][::-1] in tb[k][:4]) or (tb[i][j][::-1] in tb[k][4:]):
                c += 1
    return c

v = [(k, cnt(tb, k)) for k in tb]
vc = [x for x in v if x[1] == 2]

print(vc[0][0]*vc[1][0]*vc[2][0]*vc[3][0])
