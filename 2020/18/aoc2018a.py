# Copyright (c) 2020 Jonas Thorsell
import sys

def ev(s):
    acc = 0
    op = '+'
    while len(s):
        c = s.pop(0)
        if c.isdigit():
            n = int(c)
        if c == '(':
            n = ev(s)
        if not len(s) or c == '+' or c == '*' or c == ')':
            if op == '*':
                acc *= n
            elif op == '+':
                acc += n
            op = c
            if op == ')':
                break
    return acc

r = [ev(list(l.strip())) for l in sys.stdin]
print(r)
print(sum(r))
