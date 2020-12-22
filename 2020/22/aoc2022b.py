# Copyright (c) 2020 Jonas Thorsell
import sys

d=[[],[]]
for p in range(2):
    sys.stdin.readline()
    for l in sys.stdin:
        if not l.strip():
            break
        d[p].append(int(l))

def score(d):
    return sum([(i+1)*c for i,c in enumerate(d[::-1])])

def rc(d0, d1, g):
    h = {}
    while len(d0) and len(d1):
        w = 0
        if str((d0, d1)) in h:
            return (0, score(d0))
        h[str((d0, d1))] = True
        c0 = d0.pop(0)
        c1 = d1.pop(0)
        if len(d0) >= c0 and len(d1) >= c1:
            w, _ = rc(d0[:c0].copy(), d1[:c1].copy(), g + 1)
        else:
            w = 0 if c0 > c1 else 1
        if w == 0:
            d0.append(c0)
            d0.append(c1)
        else:
            d1.append(c1)
            d1.append(c0)

    return (0, score(d0)) if w == 0 else (1, score(d1))

w, s = rc(d[0], d[1], 1)
print(f'W {w+1} score: {s}')