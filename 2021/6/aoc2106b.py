# Copyright (c) 2021 Jonas Thorsell
import sys
from collections import defaultdict

tl = [0] * 9
for t in [int(x) for x in sys.stdin.readline().split(',')]:
    tl[t] += 1

for d in range(256):
    ntl = [0] * 9
    for i in range(9):
        if i == 0:
            ntl[8] = tl[0]
            ntl[6] = tl[0]
        else:
            ntl[i-1] += tl[i]
    tl = ntl

print(sum(tl))
