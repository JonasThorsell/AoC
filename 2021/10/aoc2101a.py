# Copyright (c) 2021 Jonas Thorsell
import sys

m = {')':'(', ']':'[', '}':'{', '>':'<'}
p = {')':3, ']':57, '}':1197, '>':25137}
tp = 0
for l in sys.stdin:
    s = []
    for c in l.strip():
        if c in ['(','[','{','<']:
            s.append(c)
        else:
            if m[c] != s.pop():
                tp += p[c]
                break
print(tp)
