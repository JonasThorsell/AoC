# Copyright (c) 2021 Jonas Thorsell
import sys

s = [int(l) for l in sys.stdin]
d = [d1 > d0 for d0, d1 in zip(s, s[1:])]
print(sum(d))
