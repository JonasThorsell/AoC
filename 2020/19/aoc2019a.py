# Copyright (c) 2020 Jonas Thorsell
import sys

def tst0(rl,s):
    r, p = tst(rl, 0, s)
    return r and p == len(s)

def tst(rl, ri, s):
    for r in rl[ri]:
        p = 0
        m = True
        for ri in r:
            if isinstance(ri, str):
                if (s[0] == ri):
                    return True, 1
                else:
                    m = False
            else:
                m, np = tst(rl, ri, s[p:])
                if not m:
                    m = False
                    break
                p += np
        if m:
            return True, p
    return False, 0

rl = {}
for l in sys.stdin:
    if not l.strip():
        break

    n, r = l.strip().split(':')
    n = int(n)
    if '"' in r:
        r = [[r.strip()[1]]]
    elif '|' in r:
        r = [[int(n) for n in x.strip().split(' ')] for x in r.split('|')]
    else:
        r = [[int(n) for n in r.strip().split(' ')]]

    rl[n] = r

m = []
for l in sys.stdin:
    m.append(l.strip())

mm = [x for x in m if tst0(rl, x)]

print(len(mm))
