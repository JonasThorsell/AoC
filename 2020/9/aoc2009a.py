# Copyright (c) 2020 Jonas Thorsell
import sys

n=[]
for l in sys.stdin:
    n.append(int(l))

pre = 25

for i in range(pre, len(n)):
    n[i]
    ok = False
    for j in range(i-pre, i):
        c = n[i] - n[j]
        if (not c == n[j] and c in n[i-pre:i]):
            ok = True
            break
    if not ok:
        print(f'Invalid {i}: {n[i]}')
        break
