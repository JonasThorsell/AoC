# Copyright (c) 2021 Jonas Thorsell
import sys
import math

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
#
# x = v0x * t - 0.5 * t^2
# vx = v0x - t
# ax = -1 (if vx > 0)
#
# vx = 0 -> t = v0x
# x = txmin -> txmin = v0x * v0x - 0.5 * v0X^2 -> v0x = sqrt(2 * txmin)

v0ymax = -tymin - 1
v0ymin = tymin - 1
v0xmax = txmax + 1
v0xmin = math.floor(math.sqrt(2 * txmin))

def simulate(v0x, v0y):
    global txmin, txmax, tymin, tymax
    x, y  = 0, 0
    vx, vy = v0x, v0y
    while y >= tymin:
        x += vx
        y += vy
        if vx > 0: vx -= 1
        vy -= 1
        if txmin <= x <= txmax and tymin <= y <= tymax:
            return True
    return False

sol = []
for v0x in range(v0xmin,v0xmax+1):
    for v0y in range(v0ymin,v0ymax+1):
        if simulate(v0x, v0y):
            sol.append((v0x,v0y))

print(len(sol))
