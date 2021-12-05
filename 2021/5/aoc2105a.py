# Copyright (c) 2021 Jonas Thorsell
import sys
import re
import numpy as np

def line(c,x1,y1,x2,y2):
    for x in range(min(x1,x2),max(x1,x2)+1):
        for y in range(min(y1,y2),max(y1,y2)+1):
            c[x,y] = c[x,y]+1

p = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
ln = []
for l in sys.stdin:
    m = [int(x) for x in p.search(l).groups()]
    if m[0] == m[2] or m[1] == m[3]:
        ln.append(m)
ln = np.array(ln)

m = ln.max(axis=0)
xm = max(m[0],m[2])
ym = max(m[1],m[3])
c = np.zeros((xm+1,ym+1), dtype=np.uint)
for l in ln:
    line(c,l[0],l[1],l[2],l[3])
print(c.T)

print(np.sum(c >= 2))
