import sys



vmap = {}
for l in sys.stdin:
    ls=l.split()
    n = ls[1]
    f = int(ls[4][5:-1])
    e = [x[:2] for x in ls[9:]]
    vmap[n] = (f,e)
print(vmap)
opv = set()
pos = 'AA'
time = 0
rpres = 0

def value(h):
    dt=0
    s=0
    for i in h:
        dt+=1
        if len(i)>2:
            s+=max(0,(8-dt)*vmap[i[1:]][0])
    return s

def searchpath(p,h=[],r=[]):
    if len(h) > 6:
        val = value(h)
        r.append((val,h))
    else:
        op = f'O{p}'
        if (not p in opv) and (not op in h):
            hc=h.copy()
            hc.append(op)
            searchpath(p,hc,r)
        for x in vmap[p][1]:
            hc=h.copy()
            hc.append(x)
            searchpath(x,hc,r)
    return r


while time<30:
    time+=1
    print(f'== Minute',time,'@',pos)
    ar=sum([vmap[x][0] for x in opv])
    rpres+=ar
    print(sorted(list(opv)))
    print(ar,'(',rpres,')')

    rl = searchpath(pos, list(), list())
    rl=sorted(rl,reverse=True)
    print(rl[0])

    if (rl and len(rl[0][1][0])>2):
        print('Open',pos)
        opv.add(pos)
    elif(rl):
        print('Move',rl[0][1][0])
        pos=rl[0][1][0]
    else:
        print('NOP')

print(rpres)
