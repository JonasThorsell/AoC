# Copyright (c) 2020 Jonas Thorsell
import sys

def nbr(t,d):
    nt = t
    if d == 0 or d == 'ne':
        if (t[1] % 2) == 1:
            nt = (t[0]+1,t[1]-1)
        else:
            nt = (t[0],t[1]-1)
    elif d == 1 or d == 'e':
        nt = (t[0]+1,t[1])
    elif d == 2 or d == 'se':
        if (t[1] % 2) == 1:
            nt = (t[0]+1,t[1]+1)
        else:
            nt = (t[0],t[1]+1)
    elif d == 3 or d == 'sw':
        if (t[1] % 2) == 0:
            nt = (t[0]-1,t[1]+1)
        else:
            nt = (t[0],t[1]+1)
    elif d == 4 or d == 'w':
        nt = (t[0]-1,t[1])
    elif d == 5 or d == 'nw':
        if (t[1] % 2) == 0:
            nt = (t[0]-1,t[1]-1)
        else:
            nt = (t[0],t[1]-1)
    else:
        raise ValueError
    return nt

class nbri:
    def __init__(self, tile=(0,0)):
        self.t = tile
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < 6:
            nt = nbr(self.t, self.i)
            self.i += 1
            return nt
        else:
            raise StopIteration

def s2c(s):
    t = (0,0)
    p = ''
    for c in s:
        if c == 'n' or c == 's':
            p = c
        elif c == 'e' or c == 'w':
            t = nbr(t, p+c)
            p = ''
        else:
            raise ValueError
    return t

def cntnbr(t0, tc):
    c = 0
    for t in nbri(tc):
        if t in t0 and t0[t]:
            c += 1
    return c

def gol1(t0, t):
    n = cntnbr(t0, t)
    if t in t0 and t0[t]:
        return False if (n == 0) or (n > 2) else True
    else:
        return True if n == 2 else False

def gol(t0):
    t1 = {}
    for t in t0:
        if not t in t1:
            t1[t] = gol1(t0, t)
        for tn in nbri(t):
            if not tn in t1:
                t1[tn] = gol1(t0, tn)
    return t1

t0 = {}
for l in sys.stdin:
    c = s2c(l.strip())
    if c in t0:
        t0[c] = not t0[c]
    else:
        t0[c] = True

print(f'Day 0: {list(t0.values()).count(True)}')

for i in range(100):
    t0 = gol(t0)
    print(f'Day {i+1}: {list(t0.values()).count(True)}')

print(list(t0.values()).count(True))
