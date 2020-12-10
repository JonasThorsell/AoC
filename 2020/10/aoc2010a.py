# Copyright (c) 2020 Jonas Thorsell
import sys

n=[]
for l in sys.stdin:
    n.append(int(l))

n.sort()
d = [n[0]] + [b-a for a,b in zip(n, n[1:])] + [3]

p = d.count(1) * d.count(3)

print(p)
