# Copyright (c) 2021 Jonas Thorsell
import sys

a = 0
for box in sys.stdin:
    l,w,h = [int(x) for x in box.split('x')]
    s = sorted([l*w, w*h, h*l])
    a = a + s[0] + 2 * sum(s)
print(a)
