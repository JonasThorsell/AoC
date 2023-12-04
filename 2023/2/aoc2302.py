import sys
bag = {'r': 12, 'g': 13, 'b': 14}
s1 = 0
s2 = 0
for l in sys.stdin:
    gameId, sets = l.strip().split(':')
    gameId = int(gameId.split()[-1])
    sets = [{y.split()[1][0]: int(y.split()[0]) for y in x.split(',')} for x in sets.split(';')]
    possible = True
    power  = {'r': 0, 'g': 0, 'b': 0}
    for s in sets:
        for k in bag:
            if k in s and s[k]>bag[k]:
                possible = False
        for k in power:
            if k in s and s[k]>power[k]:
                power[k] = s[k]
    if possible:
        s1 += gameId
    s2 += power['r'] * power['g'] * power['b']

print(s1)
print(s2)
