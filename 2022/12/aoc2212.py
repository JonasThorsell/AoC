import sys

m = []
y = 0
sx,sy,ex,ey = 0,0,0,0
for l in sys.stdin:
    h = [ord(c)-ord('a') for c in l.strip()]
    if ord('S')-ord('a') in h:
        x = h.index(ord('S')-ord('a'))
        h[x] = 0
        sx,sy = x,y
    if ord('E')-ord('a') in h:
        x = h.index(ord('E')-ord('a'))
        h[x] = ord('z')-ord('a')
        ex,ey = x,y
    m.append(h)
    y += 1

w,h = len(m[0]), len(m)
d = [ [999] * w for _ in range(h)]
d[ey][ex] = 0

def maze(x,y):
    nd = d[y][x]+1
    me = m[y][x]-1
    if (y>0) and (m[y-1][x] >= me) and (nd < d[y-1][x]):
        d[y-1][x] = nd
        maze(x,y-1)
    if (y<h-1) and (m[y+1][x] >= me) and (nd < d[y+1][x]):
        d[y+1][x] = nd
        maze(x,y+1)
    if (x>0) and (m[y][x-1] >= me) and (nd < d[y][x-1]):
        d[y][x-1] = nd
        maze(x-1,y)
    if (x<w-1) and (m[y][x+1] >= me) and (nd < d[y][x+1]):
        d[y][x+1] = nd
        maze(x+1,y)

sys.setrecursionlimit(2000)
maze(ex,ey)
print(d[sy][sx])
dl = [d[y][x] for y in range(h) for x in range(w) if m[y][x] == 0]
print(sorted(dl)[0])
