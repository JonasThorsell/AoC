# Copyright (c) 2021 Jonas Thorsell
import sys

s = {}

def ev(w):
    if w.isnumeric():
        return int(w)
    if len(s[w]) == 1:
        s[w] = [str(ev(s[w][0]))]
    elif len(s[w]) == 2:
        s[w] = [str((~ev(s[w][1])) & 0xFFFF)]
    elif len(s[w]) == 3:
        if s[w][1] == 'AND':
            s[w] = [str((ev(s[w][0]) & ev(s[w][2])) & 0xFFFF)]
        elif s[w][1] == 'OR':
            s[w] = [str((ev(s[w][0]) | ev(s[w][2])) & 0xFFFF)]
        elif s[w][1] == 'LSHIFT':
            s[w] = [str((ev(s[w][0]) << ev(s[w][2])) & 0xFFFF)]
        elif s[w][1] == 'RSHIFT':
            s[w] = [str((ev(s[w][0]) >> ev(s[w][2])) & 0xFFFF)]
    return int(s[w][0])

for l in sys.stdin:
    i = l.split()
    s[i[-1]] = i[:-2]

s['b'] = ['46065']
print(ev('a'))
