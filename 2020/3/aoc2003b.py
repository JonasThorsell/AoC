# Copyright (c) 2020 Jonas Thorsell
import sys
import functools

m=[]
for l in sys.stdin:
    m.append(l.strip())

def cnt(m, dx, dy):
    x, y, t = 0, 0, 0
    while (y < len(m)):
        if m[y][x] == '#':
            t += 1
        x = (x + dx) % len(m[y])
        y = y + dy
    return t

tl = []
tl.append(cnt(m, 1, 1))
tl.append(cnt(m, 3, 1))
tl.append(cnt(m, 5, 1))
tl.append(cnt(m, 7, 1))
tl.append(cnt(m, 1, 2))
print(tl)
print(functools.reduce(lambda a,b : a*b, tl))


