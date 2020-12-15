# Copyright (c) 2020 Jonas Thorsell
import sys

n = [int(x) for x in sys.stdin.readline().split(',')]
m = {}
for i in range(len(n)-1):
    m[n[i]] = i

x=n[-1]
for i in range(len(n)-1, 30000000-1):
    if x in m:
        nx = i-m[x]
    else:
        nx = 0
    m[x] = i
    x=nx

print(x)
