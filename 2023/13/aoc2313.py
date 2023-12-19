import sys
import numpy as np

def fref(ptrn):
    p = np.array(ptrn)
    w,h = p.shape[1], p.shape[0]
    c0 = 0
    for c in range(w-1 if w%2==0 else w-2,0,-2):
        if (p[:,c0] == p[:,c]).all():
            eq = True
            for d in range(1,c//2+1):
                if not (p[:,c0+d] == p[:,c-d]).all():
                    eq = False
                    break
            if eq:
                return (c+1)//2
    c0 = w-1
    for c in range(0 if w%2==0 else 1,w-1,2):
        if (p[:,c0] == p[:,c]).all():
            eq = True
            for d in range(1,(c0-c)//2+1):
                if not (p[:,c0-d] == p[:,c+d]).all():
                    eq = False
                    break
            if eq:
                return (c+1)+((c0-(c+1))//2)
    r0 = 0
    for r in range(h-1 if h%2==0 else h-2,0,-2):
        if (p[r0,:] == p[r,:]).all():
            eq = True
            for d in range(1,r//2+1):
                if not (p[r0+d,:] == p[r-d,:]).all():
                    eq = False
                    break
            if eq:
                return 100*((r+1)//2)
    r0 = h-1
    for r in range(0 if h%2==0 else 1,h-1,2):
        if (p[r0,:] == p[r,:]).all():
            eq = True
            for d in range(1,(r0-r)//2+1):
                if not (p[r0-d,:] == p[r+d,:]).all():
                    eq = False
                    break
            if eq:
                return 100*((r+1)+((r0-(r+1))//2))
    return 0

s1 = 0
ptrn = []
for l in sys.stdin:
    if len(l)>1:
        ptrn.append([1 if x=='#' else 0 for x in l.strip()])
    else:
        s1 += fref(ptrn)
        ptrn = []
s1 += fref(ptrn)
print(s1)
