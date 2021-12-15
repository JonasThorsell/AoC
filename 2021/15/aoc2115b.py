# Copyright (c) 2021 Jonas Thorsell
import sys
import heapq
import numpy as np

im = []
for l in sys.stdin:
    im.append([int(rl) for rl in l.strip()])
im = np.array(im)
w=len(im[0])*5
h=len(im)*5
m = np.zeros((h,w), dtype=np.uint)
for y in range(h):
    for x in range(w):
        d=y//(h/5)+x//(w/5)
        m[y,x]=im[y%(h//5)][x%(w//5)]+d
        if m[y,x]>9:m[y,x]-=9

c = np.full_like(m, 9999999)
c[0,0] = 0
nbs = [(0,1),(0,-1),(1,0),(-1,0)]
hq = []
heapq.heappush(hq, (0, (0,0)))
goal = (m.shape[0]-1,m.shape[1]-1)
while hq:
    mc,p = heapq.heappop(hq)
    if mc>c[goal]:
        break
    for dy,dx in nbs:
        nb=(p[0]+dy,p[1]+dx)
        if 0<=nb[0]<m.shape[0] and 0<=nb[1]<m.shape[1]:
            nc = c[p]+m[nb]
            if nc < c[nb]:
                c[nb] = nc
                heapq.heappush(hq, (nc + abs(goal[0]-nb[0])+abs(goal[1]-nb[1]), nb))

print(c[goal])
