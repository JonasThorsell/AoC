# Copyright (c) 2021 Jonas Thorsell
import sys

for l in sys.stdin:
    h = {}
    p = (0,0)
    h[p] = 1
    for c in l:
        if c == '^': p = (p[0], p[1]-1)
        if c == 'v': p = (p[0], p[1]+1)
        if c == '<': p = (p[0]-1, p[1])
        if c == '>': p = (p[0]+1, p[1])
        if p in h:
            h[p] = h[p] + 1
        else:
            h[p] = 1
    print(len(h))
