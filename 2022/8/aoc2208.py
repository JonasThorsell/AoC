import sys

def vis(m,w,h,x,y):
    if x == 0 or x == w-1 or y == 0 or y == h-1:
        return 1
    if max([m[y][i] for i in range(x)]    ) < m[y][x] or \
       max([m[y][i] for i in range(x+1,w)]) < m[y][x] or \
       max([m[i][x] for i in range(y)]    ) < m[y][x] or \
       max([m[i][x] for i in range(y+1,h)]) < m[y][x]:
       return 1
    return 0

def scenic(m,w,h,x,y):
    if x == 0 or x == w-1 or y == 0 or y == h-1:
        return 0
    sn,se,ss,sw=0,0,0,0
    i=y-1
    while i>=0:
        sn+=1
        if m[i][x]>=m[y][x]:
            break
        i-=1
    i=y+1
    while i<h:
        ss+=1
        if m[i][x]>=m[y][x]:
            break
        i+=1
    i=x-1
    while i>=0:
        sw+=1
        if m[y][i]>=m[y][x]:
            break
        i-=1
    i=x+1
    while i<w:
        se+=1
        if m[y][i]>=m[y][x]:
            break
        i+=1
    return sn*se*ss*sw


m = []

for l in sys.stdin:
    m.append([int(x) for x in l.strip()])

w,h = len(m[0]),len(m)

s1,s2 = 0,0
for y in range(h):
    for x in range(w):
        s1 += vis(m,w,h,x,y)
        s2 = max(s2,scenic(m,w,h,x,y))

print(s1)
print(s2)
