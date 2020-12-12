# Copyright (c) 2020 Jonas Thorsell
import sys
import math

n=[]
for l in sys.stdin:
    n.append((l[0], int(l[1:])))

sx, sy = 0, 0
wx, wy = 10, 1

for i in n:
    if (i[0] == 'N'):
        wy += i[1]
    elif (i[0] == 'S'):
        wy -= i[1]
    elif (i[0] == 'E'):
        wx += i[1]
    elif (i[0] == 'W'):
        wx -= i[1]
    elif (i[0] == 'L'):
        c = int(math.cos(math.radians(i[1])))
        s = int(math.sin(math.radians(i[1])))
        wx, wy = wx * c - wy * s, wx * s + wy * c
    elif (i[0] == 'R'):
        c = int(math.cos(math.radians(-i[1])))
        s = int(math.sin(math.radians(-i[1])))
        wx, wy = wx * c - wy * s, wx * s + wy * c
    elif (i[0] == 'F'):
        sx += wx * i[1]
        sy += wy * i[1]
    else:
        print(f"Unknown instruction {i[0]}")

print(f"Dist {sx},{sy} = {abs(sx)+abs(sy)}")
