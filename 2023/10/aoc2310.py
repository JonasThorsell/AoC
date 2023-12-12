import sys

map = []
for l in sys.stdin:
    map.append(l)

c0, r0 = -1, -1
for r in range(len(map)):
    if c0 < 0 and (c0 := map[r].find("S")) >= 0:
        r0 = r
        break

c,r,d = c0,r0,0
if r>0 and map[r-1][c] in ['|', 'F', '7']:
    r -= 1
    d = 0
elif c<len(map[0])-1 and map[r][c+1] in ['|', 'J', '7']:
    c += 1
    d = 1
elif r<len(map)-1 and map[r+1][c] in ['|', 'J', 'L']:
    r += 1
    d = 2
elif c>0 and map[r][c-1] in ['-', 'F', 'L']:
    c -= 1
    d = 3
else:
    print('Error', r, c, 'S')

s = 1
while not r==r0 or not c==c0:
    s += 1
    t = map[r][c]
    if (d==0 and t == '|') or (d==1 and t == 'J') or (d==3 and t == 'L'):
        d=0
        r-=1
    elif (d==1 and t == '-') or (d==0 and t == 'F') or (d==2 and t=='L'):
        d=1
        c+=1
    elif (d==2 and t == '|') or (d==1 and t == '7') or (d==3 and t=='F'):
        d=2
        r+=1
    elif (d==3 and t == '-') or (d==0 and t == '7') or (d==2 and t=='J'):
        d=3
        c-=1
    else:
        print('Error', r, c, t)

print(s//2)
