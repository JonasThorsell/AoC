# Copyright (c) 2020 Jonas Thorsell
import sys

n=[]
for l in sys.stdin:
    n.append(int(l))

n.sort()
d = [n[0]] + [b-a for a,b in zip(n, n[1:])] + [3]

v = [1,1,2,4,7]
c, s = 0, 1
for i in range(len(d)):
    if (d[i] == 1):
        c += 1
    else:
        s *= v[c]
        c = 0

print(s)
