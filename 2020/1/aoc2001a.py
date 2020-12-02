# Copyright (c) 2020 Jonas Thorsell
import sys

n=[]
for l in sys.stdin:
    n.append(int(l))

for x in n:
    if (2020-x) in n:
        print(f"{x} * {2020-x} = {x*(2020-x)}")
        quit()
