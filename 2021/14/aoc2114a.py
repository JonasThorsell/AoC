# Copyright (c) 2021 Jonas Thorsell
import sys
from collections import defaultdict
from collections import Counter

pt = sys.stdin.readline().strip()
sys.stdin.readline()
pir = defaultdict(str)
for l in sys.stdin:
    p,i = l.strip().split(' -> ')
    pir[p] = i

for s in range(10):
    next = ''
    for i in range(len(pt)-1):
        next += pt[i] + pir[pt[i:i+2]]
    next += pt[-1]
    pt = next

cnt = Counter(pt).most_common()
print(cnt[0][1]-cnt[-1][1])
