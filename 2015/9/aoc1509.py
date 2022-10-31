# Copyright (c) 2022 Jonas Thorsell
import sys
import itertools

dmap = {}
for l in sys.stdin:
    w = l.strip().split()
    l0, l1, d = w[0], w[2], int(w[4])
    if not l0 in dmap:
        dmap[l0] = {}
    if not l1 in dmap:
        dmap[l1] = {}
    dmap[l0][l1] = d
    dmap[l1][l0] = d

locs = dmap.keys()
routes = list(itertools.permutations(locs))
rd = {}
for r in routes:
    d = 0
    for p in range(len(r)-1):
        d += dmap[r[p]][r[p+1]]
    rd[r] = d

shortest = sorted(rd, key=rd.get)[0]
print(shortest, rd[shortest])

longest = sorted(rd, key=rd.get)[-1]
print(longest, rd[longest])
