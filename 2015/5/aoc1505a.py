# Copyright (c) 2021 Jonas Thorsell
import sys

vowelstr = 'aeiou'
badstr = ['ab', 'cd', 'pq', 'xy']
nice = 0
for l in sys.stdin:
    l = l.strip()
    vc, tc, bc = 0, 0, 0
    for i in range(0, len(l)):
        if l[i] in vowelstr:
            vc=vc+1
        if i < len(l)-1 and l[i] == l[i+1]:
            tc=tc+1
        if i < len(l)-1 and l[i:i+2] in badstr:
            bc=bc+1
    if vc >= 3 and tc and not bc:
        nice += 1

print(nice)
