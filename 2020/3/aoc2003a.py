# Copyright (c) 2020 Jonas Thorsell
import sys

m=[]
for l in sys.stdin:
    m.append(l.strip())

x, t = 0, 0
for y in range(len(m)):
    if m[y][x] == '#':
        t += 1
    x = (x + 3) % len(m[y])

print(t)
