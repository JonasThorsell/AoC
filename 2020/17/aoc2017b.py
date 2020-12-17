# Copyright (c) 2020 Jonas Thorsell
import sys

def cntn(p, s):
    c = 0
    for x in range(p[0]-1, p[0]+2):
        for y in range(p[1]-1, p[1]+2):
            for z in range(p[2]-1, p[2]+2):
                for w in range(p[3]-1, p[3]+2):
                    if not p == (x, y, z, w) and (x, y, z, w) in s and s[(x, y, z, w)]:
                        c += 1
    return c

s0={}
for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l.strip()):
        if c == '#':
            s0[(x,y,0,0)] = True
print(f"0: {sum([1 for x in s0.keys() if s0[x]])}")

for i in range(6):
    sn = {}
    for p in s0.keys():
        if s0[p]:
            for x in range(p[0]-1, p[0]+2):
                for y in range(p[1]-1, p[1]+2):
                    for z in range(p[2]-1, p[2]+2):
                        for w in range(p[3]-1, p[3]+2):
                            sn[(x,y,z,w)] = False

    for p in sn.keys():
        if p in s0 and s0[p]:
            if 2 <= cntn(p, s0) <= 3:
                sn[p] = True
        else:
            if cntn(p, s0) == 3:
                sn[p] = True

    print(f"{i+1}: {sum([1 for x in sn.keys() if sn[x]])}")
    s0 = sn
