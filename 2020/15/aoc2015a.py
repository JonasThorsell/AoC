# Copyright (c) 2020 Jonas Thorsell
import sys

n = [int(x) for x in sys.stdin.readline().split(',')]
n.reverse()

for i in range(2020-len(n)):
    if n[0] in n[1:]:
        n.insert(0, n[1:].index(n[0])+1)
    else:
        n.insert(0, 0)

print(n[0])
