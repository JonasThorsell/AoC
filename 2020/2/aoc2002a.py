# Copyright (c) 2020 Jonas Thorsell
import sys

n=0
for l in sys.stdin:
    r, c, p = l.split()
    r0, r1 = [int(x) for x in r.split('-')]
    c = c[0]
    if (r0 <= p.count(c) <= r1):
        n += 1

print(n)
