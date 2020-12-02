# Copyright (c) 2020 Jonas Thorsell
import sys
from bisect import bisect_left

n=[]
for l in sys.stdin:
    n.append(int(l))
n.sort()

for i in range(len(n)):
    for j in range(len(n)-i-1):
        k = bisect_left(n, 2020-n[i]-n[j], j+1)
        if k != len(n) and n[k] == 2020-n[i]-n[j]:
            print(f"{n[i]} * {n[j]} * {n[k]} = {n[i]*n[j]*n[k]}")
            quit()
