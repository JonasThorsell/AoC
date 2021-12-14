# Copyright (c) 2021 Jonas Thorsell
import sys
from collections import defaultdict
from collections import Counter

pt = sys.stdin.readline().strip()
sys.stdin.readline()
pir = defaultdict(str)
for l in sys.stdin:
    p,i = l.strip().split(' -> ')
    pir[p] = i

elems = defaultdict(int)
for e in pt: elems[e] += 1
pairs = defaultdict(int)
for p in zip(pt[0:-1], pt[1:]): pairs[p[0]+p[1]] += 1

for s in range(40):
    pc = pairs.copy()
    for k, v in pc.items():
        pairs[k] -= v
        a = pir[k]
        pairs[k[0]+a] += v
        pairs[a+k[1]] += v
        elems[a] += v

se = sorted(elems.items(), key=lambda x: x[1])
print(se[-1][1]-se[0][1])
