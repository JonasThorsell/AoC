# Copyright (c) 2022 Jonas Thorsell
import sys

# Parse reindeer list
rdl = dict()
for l in sys.stdin:
    l = l.strip().split()
    name = l[0]
    rdl[l[0]] = {'speed': int(l[3]), 'time': int(l[6]), 'rest': int(l[13]), 'dist': 0, 'score': 0}


# Simulate race
t = 0
while t<2503:
    for k,v in rdl.items():
        # Check if flying or resting
        if t % (v['time'] + v['rest']) < v['time']:
            v['dist'] += v['speed']
    # Check who is in lead for part two scoring
    leader = sorted(rdl, key=lambda rd: rdl[rd]['dist'])[-1]
    leaderdist = rdl[leader]['dist']
    for k,v in rdl.items():
        if v['dist'] == leaderdist:
            v['score'] += 1
    t+=1

for k,v in rdl.items():
    print(k, v)

# Part one, winner by distance
winner1 = sorted(rdl, key=lambda rd: rdl[rd]['dist'])[-1]
print('Part One:', winner1, rdl[winner1]['dist'])

# Part two, winner by score
winner2 = sorted(rdl, key=lambda rd: rdl[rd]['score'])[-1]
print('Part Two:', winner2, rdl[winner2]['score'])
