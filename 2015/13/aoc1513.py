# Copyright (c) 2022 Jonas Thorsell
import sys
import itertools

# Parse happiness list
ha = dict()
for l in sys.stdin:
    l = l.strip()[:-1].split()
    if not l[0] in ha:
        ha[l[0]] = dict()
    ha[l[0]][l[10]] = int(l[3]) if l[2] == 'gain' else -int(l[3])

# Calculate change in happiness
def score(seating):
    i,s = 0,0
    while i < len(seating):
        s += ha[seating[i]][seating[(i-1)%len(seating)]]
        s += ha[seating[i]][seating[(i+1)%len(seating)]]
        i += 1
    return s

# Get all seating permutations and map them to score function
seatings = list(itertools.permutations(ha.keys()))
print(sorted(map(score, seatings))[-1])

# Add Me to happines list
gl = ha.keys()
for g in gl:
    ha[g]['Me'] = 0
ha['Me'] = dict()
for g in gl:
    ha['Me'][g] = 0

# Get all seating permutations and map them to score function
seatings = list(itertools.permutations(ha.keys()))
print(sorted(map(score, seatings))[-1])
