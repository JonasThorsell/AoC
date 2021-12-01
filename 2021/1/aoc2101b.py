# Copyright (c) 2021 Jonas Thorsell
import sys

s = [int(l) for l in sys.stdin]
w = [sum(d) for d in zip(s[:-2], s[1:-1], s[2:])]
d = [d1 > d0 for d0, d1 in zip(w, w[1:])]
print(sum(d))
