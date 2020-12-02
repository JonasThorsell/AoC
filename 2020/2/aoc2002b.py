# Copyright (c) 2020 Jonas Thorsell
import sys

n=0
for l in sys.stdin:
    r, c, p = l.split()
    r0, r1 = [int(x)-1 for x in r.split('-')]
    c = c[0]
    if ((p[r0] == c) + (p[r1] == c) == 1):
        n += 1

print(n)
