import sys
import itertools
import copy

def expand(u):
    y = 0
    while y < len(u):
        if not '#' in u[y]:
            u.insert(y, list('.' * len(u[0])))
            y += 1
        y += 1
    x = 0
    while x < len(u[0]):
        if not '#' in [u[y][x] for y in range(len(u))]:
            for y in range(len(u)):
                u[y].insert(x,'.')
            x += 1
        x += 1
    return u

def sp(a,b,u,r):
    d = 0
    for y in range(min(a[0],b[0]),max(a[0],b[0])):
        d += 1 if '#' in u[y] else r
    for x in range(min(a[1],b[1]),max(a[1],b[1])):
        d += 1 if '#' in [u[y][x] for y in range(len(u))] else r
    return d

def enumglx(u):
    g = []
    for y in range(len(u)):
        for x in range(len(u[0])):
            if (u[y][x] == '#'):
                g.append((y,x))
    return g

m = []
for l in sys.stdin:
    m.append(list(l.strip()))

em = expand(copy.deepcopy(m))
s1 = 0
for p in itertools.combinations(enumglx(em), 2):
    s1 += abs(p[0][0]-p[1][0])+abs(p[0][1]-p[1][1])
print(s1)

s2 = 0
for p in itertools.combinations(enumglx(m), 2):
    s2 += sp(p[0],p[1],m,1000000)
print(s2)
