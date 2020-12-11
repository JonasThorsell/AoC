# Copyright (c) 2020 Jonas Thorsell
import sys

n=[]
for l in sys.stdin:
    n.append(list(l.strip()))

def occ(n, x, y, dx, dy):
    x += dx
    y += dy    
    while (0 <= x < len(n[0]) and 0 <= y < len(n)):
        if (n[y][x] == '#'):
            return 1
        elif (n[y][x] == 'L'):
            return 0
        x += dx
        y += dy    
    return 0

def sumocc(n,x,y):
    return occ(n,x,y,-1,-1) + occ(n,x,y,0,-1) + occ(n,x,y,1,-1) \
        + occ(n,x,y,-1,0) + occ(n,x,y,+1,0) \
        +  occ(n,x,y,-1,1) + occ(n,x,y,0,1) + occ(n,x,y,1,1)

change = True
while change:
    change = False
    u = [['.'] * len(n[0]) for i in range(len(n))]
    for x in range(len(n[0])):
        for y in range(len(n)):
            if n[y][x] == 'L':
                if sumocc(n,x,y) == 0:
                    u[y][x] = '#'
                    change = True
                else:
                    u[y][x] = 'L'
            elif n[y][x] == '#':
                if sumocc(n,x,y) >= 5:
                    u[y][x] = 'L'
                    change = True
                else:
                    u[y][x] = '#'
    n = [u[i].copy() for i in range(len(u))]

print(sum([x.count('#') for x in n]))
