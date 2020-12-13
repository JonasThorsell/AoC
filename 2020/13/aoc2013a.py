# Copyright (c) 2020 Jonas Thorsell
import sys
import math

t = int(sys.stdin.readline())
b = [ math.inf if x == 'x' else int(x) for x in sys.stdin.readline().split(',')]
d = sorted([(x - (t % x), x) for x in b])

print(d[0][0] * d[0][1])
