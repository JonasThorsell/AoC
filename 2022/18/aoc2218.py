import sys

dirl=[[+1,0,0],[-1,0,0],[0,+1,0],[0,-1,0],[0,0,+1],[0,0,-1]]
cl = set()
for l in sys.stdin:
    c=[int(x) for x in l.split(',')]
    cl.add(tuple(c))

def trapped(p):
    pdl=set()
    pl=[p]
    while pl:
        p=pl.pop()
        pdl.add(p)
        if [1 for x in p if x>20 or x<-20]:
            return False
        for d in dirl:
            t = (p[0]+d[0],p[1]+d[1],p[2]+d[2])
            if not t in cl and not t in pdl:
                pl.append(t)
    return True

s1,s2 = 0,0
for c in cl:
    c=list(c)
    for d in dirl:
        t = (c[0]+d[0],c[1]+d[1],c[2]+d[2])
        if not t in cl:
            s1+=1
            if not trapped(t):
                s2+=1

print(s1)
print(s2)
