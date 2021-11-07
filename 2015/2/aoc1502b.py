# Copyright (c) 2021 Jonas Thorsell
import sys

l = 0
for box in sys.stdin:
    s = sorted([int(x) for x in box.split('x')])
    l += 2*(s[0] + s[1]) + s[0]*s[1]*s[2]
print(l)
