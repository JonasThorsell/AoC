# Copyright (c) 2020 Jonas Thorsell
import sys

cups = [int(x) for x in sys.stdin.readline().strip()]

def move(cups):
    pick = cups[1:4]
    cups = cups[0:1]+cups[4:]
    dl = cups[0]-1
    while not dl in cups:
        dl = (dl - 1) % 10
    di = cups.index(dl)
    cups = cups[:di+1] + pick + cups[di+1:]
    cups = cups[1:]+cups[0:1]
    return cups

for i in range(100):
    cups = move(cups)

i = cups.index(1)
cups = cups[i:] + cups[:i]
s = "".join([str(x) for x in cups[1:]])
print(s)
