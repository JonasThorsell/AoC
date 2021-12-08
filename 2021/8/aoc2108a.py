# Copyright (c) 2021 Jonas Thorsell
import sys

c = 0
for l in sys.stdin:
    o = [len(x) for x in l.strip().split('|')[1].split()]
    c += (o.count(2) + o.count(3) + o.count(4) + o.count(7))
print(c)
