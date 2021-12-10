# Copyright (c) 2021 Jonas Thorsell
import sys

m = {')':'(', ']':'[', '}':'{', '>':'<'}
p = {'(': 1, '[': 2, '{': 3, '<': 4}
tpl = []
for l in sys.stdin:
    s = []
    bad = False
    for c in l.strip():
        if c in ['(','[','{','<']:
            s.append(c)
        else:
            if m[c] != s.pop():
                bad=True
                break
    if not bad:
        tp = 0
        for c in reversed(s):
            tp *= 5
            tp += p[c]
        tpl.append(tp)
print(sorted(tpl)[len(tpl)//2])
