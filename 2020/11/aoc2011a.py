# Copyright (c) 2020 Jonas Thorsell
import sys

n=[]
for l in sys.stdin:
    n.append(list(l.strip()))

def occ(n, x, y):
    if (0 <= x < len(n[0]) and 0 <= y < len(n) and n[y][x] == '#'):
        return 1
    return 0

def sumocc(n,x,y):
    return occ(n,x-1,y-1) + occ(n,x,y-1) + occ(n,x+1,y-1) \
        + occ(n,x-1,y) + occ(n,x+1,y) \
        +  occ(n,x-1,y+1) + occ(n,x,y+1) + occ(n,x+1,y+1)

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
                if sumocc(n,x,y) >= 4:
                    u[y][x] = 'L'
                    change = True
                else:
                    u[y][x] = '#'
    n = [u[i].copy() for i in range(len(u))]

print(sum([x.count('#') for x in n]))
