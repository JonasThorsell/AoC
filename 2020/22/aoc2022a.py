# Copyright (c) 2020 Jonas Thorsell
import sys

d=[[],[]]
for p in range(2):
    sys.stdin.readline()
    for l in sys.stdin:
        if not l.strip():
            break
        d[p].append(int(l))

while len(d[0]) and len(d[1]):
    c0 = d[0].pop(0)
    c1 = d[1].pop(0)
    if c0 > c1:
        d[0].append(c0)
        d[0].append(c1)
    else:
        d[1].append(c1)
        d[1].append(c0)

s0 = sum([(i+1)*c for i,c in enumerate(d[0][::-1])])
s1 = sum([(i+1)*c for i,c in enumerate(d[1][::-1])])
print(max(s0, s1))
