# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np
from collections import defaultdict

p1start = int(sys.stdin.readline().strip()[-1])
p2start = int(sys.stdin.readline().strip()[-1])

# 3D3 3-9, 3:1 4:3 5:6 6:7 7:6 8:3 9:1
dice = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]

gst = {(0,p1start,0,p2start):1}
p1games = 0
p2games = 0

s=0
while len(gst):
    s+=1
    print(s, len(gst))
    ngst = defaultdict(int)
    for (s1,p1,s2,p2),n in gst.items():
        for o1,v1 in dice:
            np1 = p1+o1
            ns1 = s1 + (10 if (np1%10==0) else (np1%10))
            if ns1 < 21:
                for o2,v2 in dice:
                    np2 = p2+o2
                    ns2 = s2 + (10 if (np2%10==0) else (np2%10))
                    if ns2 < 21:
                        ngst[(ns1,np1,ns2,np2)] += n*v1*v2
                    else:
                        p2games += n*v1*v2
            else:
                p1games += n*v1
    gst = ngst

print('P1', p1games)
print('P2', p2games)
print(max(p1games,p2games))
