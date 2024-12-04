import sys

p = []
for l in sys.stdin:
    p.append(list(l.strip()))
s1, s2 = 0, 0
r = len(p)
c = len(p[0])
for y in range(r):
    for x in range(c):
        if x+3 <  c and 'XMAS' == p[y][x]+p[y][x+1]+p[y][x+2]+p[y][x+3]:
            s1 += 1
        if x-3 >= 0 and 'XMAS' == p[y][x]+p[y][x-1]+p[y][x-2]+p[y][x-3]:
            s1 += 1
        if y+3 <  r and 'XMAS' == p[y][x]+p[y+1][x]+p[y+2][x]+p[y+3][x]:
            s1 += 1
        if y-3 >= 0 and 'XMAS' == p[y][x]+p[y-1][x]+p[y-2][x]+p[y-3][x]:
            s1 += 1
        if x+3 <  c and y+3 <  r and 'XMAS' == p[y][x]+p[y+1][x+1]+p[y+2][x+2]+p[y+3][x+3]:
            s1 += 1
        if x-3 >= 0 and y+3 <  r and 'XMAS' == p[y][x]+p[y+1][x-1]+p[y+2][x-2]+p[y+3][x-3]:
            s1 += 1
        if x+3 <  c and y-3 >= 0 and 'XMAS' == p[y][x]+p[y-1][x+1]+p[y-2][x+2]+p[y-3][x+3]:
            s1 += 1
        if x-3 >= 0 and y-3 >= 0 and 'XMAS' == p[y][x]+p[y-1][x-1]+p[y-2][x-2]+p[y-3][x-3]:
            s1 += 1

for y in range(1,r-1):
    for x in range(1,c-1):
        if (p[y][x] == 'A') and \
            ((p[y-1][x-1] == 'M' and p[y+1][x+1] == 'S') or (p[y-1][x-1] == 'S' and p[y+1][x+1] == 'M')) and \
            ((p[y-1][x+1] == 'M' and p[y+1][x-1] == 'S') or (p[y-1][x+1] == 'S' and p[y+1][x-1] == 'M')):
            s2 += 1

print(s1)
print(s2)
