# Copyright (c) 2021 Jonas Thorsell
import sys
import math
import itertools

def addsn(a, b):
    if len(a) > 0:
        return ['['] + a + [','] + b + [']']
    else:
        return b

def explode(sns):
    d=0
    for i in range(len(sns)):
        if sns[i] == '[': d+=1
        if sns[i] == ']': d-=1
        if d>=5:
            # [a,b]
            #-i12345
            a,b = sns[i+1], sns[i+3]
            j = i + 5
            while j < len(sns) and not isinstance(sns[j], int): j += 1
            if j < len(sns):
                sns[j] += b
            j = i - 1
            while j >= 0 and not isinstance(sns[j], int): j -= 1
            if j >= 0:
                sns[j] += a
            sns = sns[:i] + [0] + sns[i+5:]
            return sns, True
    return sns, False

def split(sns):
    d=0
    for i in range(len(sns)):
        if isinstance(sns[i], int) and sns[i] > 9:
            n = sns[i]
            a = math.floor(n/2)
            b = math.ceil(n/2)
            sns = sns[:i] + ['[',a,',',b,']'] + sns[i+1:]
            return sns, True
    return sns, False

def magnitude(sn):
    if isinstance(sn[0], int):
        return sn[0]
    assert sn[0] == '['
    i=2
    if isinstance(sn[1], str):
        assert sn[1] == '['
        d=1
        while d>0:
            if isinstance(sn[i], str):
                if sn[i] == '[': d+=1
                if sn[i] == ']': d-=1
            i+=1
        assert sn[i] == ','
        i+=1
    else:
        assert sn[i] == ','
        i+=1
    n = 3 * magnitude(sn[1:]) + 2 * magnitude(sn[i:])
    return n

def psn(sn):
    return ''.join([str(x) for x in sn])

def addredmag(a, b):
    ab = addsn(a,b)
    while True:
        ab, exp = explode(ab)
        if exp: continue
        ab, spl = split(ab)
        if spl: continue
        break
    return magnitude(ab)

snl = []
for l in sys.stdin:
    snl.append([c if not c.isdecimal() else int(c) for c in l.strip()])

m = []
l = 2*int(math.factorial(len(snl))/(math.factorial(2)*math.factorial(len(snl)-2)))
i = 1
for ab in itertools.permutations(snl, 2):
    print(f'{i}/{l}')
    i+=1
    m.append(addredmag(ab[0], ab[1]))
print(sorted(m)[-1])
