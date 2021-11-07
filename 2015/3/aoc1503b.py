# Copyright (c) 2021 Jonas Thorsell
import sys

for l in sys.stdin:
    h = {}
    p = [(0,0), (0,0)]
    h[p[0]] = 2
    for i,c in enumerate(l):
        o = 1
        if i%2 == 0:
            o = 0
        if c == '^': p[o] = (p[o][0], p[o][1]-1)
        if c == 'v': p[o] = (p[o][0], p[o][1]+1)
        if c == '<': p[o] = (p[o][0]-1, p[o][1])
        if c == '>': p[o] = (p[o][0]+1, p[o][1])
        if p[o] in h:
            h[p[o]] = h[p[o]] + 1
        else:
            h[p[o]] = 1
    print(len(h))
