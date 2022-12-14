import sys
import copy

def line(m,x,y,x1,y1):
    m[y][x]='#'
    while (not x==x1) or (not y==y1):
        x += ((x<x1)-(x>x1))
        y += ((y<y1)-(y>y1))
        m[y][x]='#'

def mprint(m):
    for l in m:
        print(''.join(l))

def addsand(m,x,y,floor=False):
    if not m[y][x] == '.':
        return False
    while y<(len(m)-1):
        if floor and y == (len(m)-2):
            m[y][x]='o'
            return True
        if m[y+1][x] == '.':
            y += 1
        elif m[y+1][x-1] == '.':
            y += 1
            x -= 1
        elif m[y+1][x+1] == '.':
            y += 1
            x += 1
        else:
            m[y][x]='o'
            return True
    return False

rock = []
minx,maxx,miny,maxy=999,0,999,0
for l in sys.stdin:
    sl = l.strip().split(' -> ')
    rock.append([])
    for s in sl:
        x,y = [int(n) for n in s.split(',')]
        rock[-1].append((x,y))
        minx = min(minx,x)
        maxx = max(maxx,x)
        miny = min(miny,y)
        maxy = max(maxy,y)

w = 1000
h = maxy+3

m = [['.']*w for _ in range(h)]
for rl in rock:
    for i in range(len(rl)-1):
        line(m,rl[i][0],rl[i][1],rl[i+1][0],rl[i+1][1])

s1 = 0
m1 = copy.deepcopy(m)
while(addsand(m1,500,0,floor=False)):
    s1 += 1
print(s1)

s2 = 0
m2 = copy.deepcopy(m)
while(addsand(m2,500,0,floor=True)):
    s2 += 1
print(s2)
