# Copyright (c) 2021 Jonas Thorsell
import sys

total = 0
for l in sys.stdin:
    s =[set('abcdefg')] * 7
    t = l.strip().split('|')
    d = t[0].split()
    o = t[1].split()
    for x in d:
        if len(x) == 2: # 1
            s[0] = s[0] - set(x)
            s[1] = s[1] & set(x)
            s[2] = s[2] & set(x)
            s[3] = s[3] - set(x)
            s[4] = s[4] - set(x)
            s[5] = s[5] - set(x)
            s[6] = s[6] - set(x)
        elif len(x) == 3: # 7
            s[0] = s[0] & set(x)
            s[1] = s[1] & set(x)
            s[2] = s[2] & set(x)
            s[3] = s[3] - set(x)
            s[4] = s[4] - set(x)
            s[5] = s[5] - set(x)
            s[6] = s[6] - set(x)
        elif len(x) == 4: # 4
            s[0] = s[0] - set(x)
            s[1] = s[1] & set(x)
            s[2] = s[2] & set(x)
            s[3] = s[3] - set(x)
            s[4] = s[4] - set(x)
            s[5] = s[5] & set(x)
            s[6] = s[6] & set(x)
        elif len(x) == 5: # 2,3,5
            s[0] = s[0] & set(x)
            s[3] = s[3] & set(x)
            s[6] = s[6] & set(x)
        elif len(x) == 6: # 6,9,0
            s[0] = s[0] & set(x)
            s[2] = s[2] & set(x)
            s[3] = s[3] & set(x)
            s[5] = s[5] & set(x)
    for i in range(7):
        if len(s[i]) == 1:
            for j in range(7):
                if j != i: s[j] = s[j] - s[i]
    value=0
    for x in o:
        p = [len(w & set(x))>0 for w in s]
        n = -1
        if len(x) == 2: n = 1
        elif len(x) == 3: n = 7
        elif len(x) == 4: n = 4
        elif len(x) == 5: # 2,3,5
            if not p[1]: n = 5
            elif not p[2]: n = 2
            else: n = 3
        elif len(x) == 6:
            if not p[1]: n = 6
            elif not p[4]: n = 9
            elif not p[6]: n = 0
        else: n = 8
        value=value*10+n
    total += value
print(total)
