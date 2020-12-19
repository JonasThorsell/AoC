# Copyright (c) 2020 Jonas Thorsell
import sys

def tst0(rl,s):
    m, pl = tst(rl, 0, s)
    return m and len([p for p in pl if p == len(s)]) > 0 

def tst(rl, ri, s):
    if not s:
        return False, []
    if isinstance(rl[ri][0][0], str):
        if (s[0] == rl[ri][0][0]):
            return True, [1]
        else:
            return False, []
    
    m = False
    pl = []
    for r in rl[ri]:
        ipl = [0]
        im = True
        for iri in r:
            npl = []
            iim = False
            for p in ipl:
                sm, sp = tst(rl, iri, s[p:])
                if sm:
                    iim = True
                    npl += [x+p for x in sp]
            if not iim:
                im = False
                break
            ipl = npl
        if im:
            m = True
            pl += ipl

    pl = list(dict.fromkeys(pl))
    return m, pl

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

rl[8] = [[42],[42, 8]]
rl[11] = [[42, 31], [42, 11, 31]]

m = []
for l in sys.stdin:
    m.append(l.strip())

mm = [x for x in m if tst0(rl, x)]

print(len(mm))
