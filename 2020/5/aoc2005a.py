# Copyright (c) 2020 Jonas Thorsell
import sys

def dc(seat):
    r, c = 127, 7
    for i in range(7):
        if seat[i] == 'F':
            r -= 2 ** (6-i)
    for i in range(3):
        if seat[7+i] == 'L':
            c -= 2 ** (2-i)
    return 8 * r + c

n=[]
for l in sys.stdin:
    n.append(dc(l))

print(sorted(n)[-1])
