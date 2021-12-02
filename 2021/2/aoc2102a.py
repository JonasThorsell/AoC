# Copyright (c) 2021 Jonas Thorsell
import sys

h, d = 0, 0
for l in sys.stdin:
    c, n = l.split()
    if c == 'forward':
        h = h + int(n)
    if c == 'down':
        d = d + int(n)
    if c == 'up':
        d = d - int(n)

print(f'{h} x {d} = {h*d}')
