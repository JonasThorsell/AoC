# Copyright (c) 2021 Jonas Thorsell
import sys

tastrs = sys.stdin.readline().strip()[13:].split(', ')
txmin = int(tastrs[0][2:].split('..')[0])
txmax = int(tastrs[0][2:].split('..')[1])
tymin = int(tastrs[1][2:].split('..')[0])
tymax = int(tastrs[1][2:].split('..')[1])

# y = v0y * t - 0.5 * t^2
# vy = v0y - t
# ay = -1
#
# Using symetry vy@t-1 = vy@tpassingy+1
# vy = -tymin -> -tymin = voy - (-1) -> voy = -tymin - 1
# vy = 0 -> t = voy

v0y=-tymin-1
ymax=v0y*(v0y+1)//2
print(v0y, ymax)
