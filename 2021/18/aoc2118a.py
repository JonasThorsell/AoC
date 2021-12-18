# Copyright (c) 2021 Jonas Thorsell
import sys
import math

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
        #    print(f'Bad parse got {sn[i+1]} expected , at {i+1} in {sn}')
        i+=1
    else:
        assert sn[i] == ','
        i+=1

    n = 3 * magnitude(sn[1:]) + 2 * magnitude(sn[i:])
    return n

def psn(sn):
    return ''.join([str(x) for x in sn])

tsn = []
for l in sys.stdin:
    sn = [c if not c.isdecimal() else int(c) for c in l.strip()]
    tsn = addsn(tsn, sn)

    reduce = True
    while reduce:
        tsn, exp = explode(tsn)
        if exp == True:
            continue
        tsn, spl = split(tsn)
        if spl == True:
            continue
        reduce = False

print('Sum', psn(tsn))
print('Magnitude', magnitude(tsn))
