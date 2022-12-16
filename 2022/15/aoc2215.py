import sys
import re

sl, bl = [],[]
s1 = set()
y1 = 2000000

for l in sys.stdin:
    sx,sy,bx,by = [int(x) for x in re.findall(r'-?\d+', l)]
    print(sx,sy,bx,by)
    sl.append((sx,sy))
    bl.append((bx,by))
    d = abs(bx-sx)+abs(by-sy)
    x0,x,y=sx,sx,y1
    while abs(x-sx)+abs(y-sy) <= d:
        dx=x-x0
        s1.add((x0+dx,y))
        s1.add((x0-dx,y))
        x += 1
s1 -= set(bl)
print(len(s1))

