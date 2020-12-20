# Copyright (c) 2020 Jonas Thorsell
import sys
import numpy as np

ti = {}
tbn = {}
tbm = {}
tc = {}
for l in sys.stdin:
    if l.strip():
        i = int(l.strip()[5:-1])
        d = []
        for l in sys.stdin:
            if not l.strip():
                break
            d.append(['1' if x == '#' else '0' for x in l.strip()])
        ti[i] = np.array(d)
        tbn[i] = ( "".join(ti[i][ 0, :]), \
                   "".join(ti[i][ :,-1]), \
                   "".join(np.flipud(ti[i][-1, :])), \
                   "".join(np.flipud(ti[i][ :, 0])) )      
        tbm[i] = ( "".join(np.flipud(ti[i][ 0, :])), \
                   "".join(ti[i][ :,0]), \
                   "".join(ti[i][-1, :]), \
                   "".join(np.flipud(ti[i][ :, -1])) )
        tc[i] = [0, 0, 0, 0]

def fcon(tb, i):
    c = 0
    for k in tb:
        if k == i:
            continue
        for j in range(4):
            if tbn[i][j][::-1] in tbn[k]:
                if not tc[i][j] == 0:
                    print('Double!')
                tc[i][j] = k
            if tbn[i][j][::-1] in tbm[k]:
                if not tc[i][j] == 0:
                    print('Double!')
                tc[i][j] = -k

for k in tc:
    fcon(tc, k)

def rott(i):
    tc[i] = np.roll(tc[i], 1)
    tbn[i] = np.roll(tbn[i], 1)
    tbm[i] = np.roll(tbm[i], 1)
    ti[i] = np.rot90(ti[i], -1)

def flipt(i):
    t = tc[i][0]
    tc[i][0] = -tc[i][2]
    tc[i][1] = -tc[i][1]
    tc[i][2] = -t
    tc[i][3] = -tc[i][3]
    t = tbn[i]
    tbn[i] = tbm[i]
    tbm[i] = t
    ti[i] = np.flipud(ti[i])


c0 = [x for x in tc if tc[x].count(0) == 2][0]
while (not tc[c0][0] == 0) or (not tc[c0][3] == 0):
    rott(c0)

s = int(len(tc) ** 0.5)
tf = np.zeros((s,s))
tf[0,0] = c0
for x in range(1, s):
    n = tc[tf[0,x-1]][1]
    if n < 0:
        n = -n
        flipt(n)
    while not abs(tc[n][3]) == tf[0,x-1]:
        rott(n)
    tf[0,x] = n

for y in range(1, s):
    for x in range(s):
        n = tc[tf[y-1,x]][2] 
        if n < 0:
            n = -n
            flipt(n)
        while not abs(tc[n][0]) == tf[y-1,x]:
            rott(n)
        tf[y,x] = n

sp = s*8
tp = np.zeros((sp,sp))

for y in range(sp):
    for x in range(sp):
        yy = y // 8
        yo = y % 8
        xx = x // 8
        xo = x % 8
        t = tf[yy,xx]
        tp[y,x] = ti[t][1+yo,1+xo]


def plot(m):
    for y in range(sp):
        print("".join(['#' if x == 1 else '@' if x > 1 else '.' for x in m[y,:]]))

def match1(yy,xx,p):
    for y in range(p.shape[0]):
        for x in range(p.shape[1]):
            if p[y,x] and not tp[yy+y,xx+x]:
                return False
    return True

def mark1(yy,xx,p):
    for y in range(p.shape[0]):
        for x in range(p.shape[1]):
            if p[y,x]:
                tp[yy+y,xx+x] += 1

def mark(p):
    for y in range(sp-p.shape[0]):
        for x in range(sp-p.shape[1]):
            if match1(y,x,p):
                mark1(y,x,p)

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
p = np.array([\
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],\
    [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],\
    [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]])

for i in range(3):
    mark(np.rot90(p,i))
    mark(np.rot90(np.flipud(p),i))

plot(np.fliplr(np.rot90(tp, -1)))

print((tp == 1).sum())

