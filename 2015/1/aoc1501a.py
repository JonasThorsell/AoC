# Copyright (c) 2021 Jonas Thorsell
import sys

for l in sys.stdin:
    floor = 0
    for c in l:
        if c == '(':
            floor = floor + 1
        if c == ')':
            floor = floor - 1
    print(floor)
