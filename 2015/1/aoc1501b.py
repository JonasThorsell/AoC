# Copyright (c) 2021 Jonas Thorsell
import sys

for l in sys.stdin:
    floor = 0
    for i,c in enumerate(l,1):
        if c == '(':
            floor = floor + 1
        if c == ')':
            floor = floor - 1
        if floor == -1:
            print(i)
            break
