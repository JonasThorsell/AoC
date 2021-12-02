# Copyright (c) 2021 Jonas Thorsell
import sys

h, d, a = 0, 0, 0
for l in sys.stdin:
    c, n = l.split()
    if c == 'forward':
        h = h + int(n)
        d = d + a * int(n)
    if c == 'down':
        a = a + int(n)
    if c == 'up':
        a = a - int(n)

print(f'{h} x {d} = {h*d}')
