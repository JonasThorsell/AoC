# Copyright (c) 2021 Jonas Thorsell
import sys

p1start = int(sys.stdin.readline().strip()[-1])
p2start = int(sys.stdin.readline().strip()[-1])

r, p1s, p2s, s = 0, 0, 0, 0
p1, p2 = p1start, p2start
while True:
    s = (r+1)%100+(r+2)%100+(r+3)%100
    r += 3
    p1 = (p1+s)%10
    if p1==0: p1=10
    p1s += p1
    if p1s >= 1000:
        print(p2s * r)
        break
    s = (r+1)%100+(r+2)%100+(r+3)%100
    r += 3
    p2 = (p2+s)%10
    if p2==0: p2=10
    p2s += p2
    if p2s >= 1000:
        print(p1s * r)
        break
