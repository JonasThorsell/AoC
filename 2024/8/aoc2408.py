import sys
import itertools
import math

al = []
h,w=0,0
for l in sys.stdin:
    l=l.strip()
    h+=1
    if not w:
        w = len(l)
    for i,c in enumerate(l):
        if c!='.':
            al.append((c,i,h-1))

fl = set([x[0] for x in al])

anl1=[]
anl2=[]
for f in fl:
    p=[(x[1],x[2]) for x in al if x[0]==f]
    for a in itertools.combinations(p,2):
        dx = a[0][0]-a[1][0]
        dy = a[0][1]-a[1][1]
        
        an1=(a[0][0]+dx, a[0][1]+dy)
        an2=(a[1][0]-dx, a[1][1]-dy)
        if 0<=an1[0]<w and 0<=an1[1]<h:
            anl1.append(an1)
        if 0<=an2[0]<w and 0<=an2[1]<h:
            anl1.append(an2)

        cd = math.gcd(dx,dy)
        dx, dy = dx//cd, dy//cd

        x,y = a[0][0], a[0][1]
        while 0<=x<w and 0<=y<h:
            anl2.append((x,y))
            x,y = x+dx, y+dy
        x,y = a[0][0]-dx, a[0][1]-dy
        while 0<=x<w and 0<=y<h:
            anl2.append((x,y))
            x,y = x-dx, y-dy


print(len(set(anl1)))
print(len(set(anl2)))
