# Copyright (c) 2020 Jonas Thorsell
import sys
import functools

def ev(s):
    stack = []
    op = '*'
    while len(s):
        c = s.pop(0)
        if c.isdigit():
            n = int(c)
        if c == '(':
            n = ev(s)
        if not len(s) or c == '+' or c == '*' or c == ')':
            if op == '*':
                stack.append(n)
            elif op == '+':
                stack[-1] = stack[-1]+n
            op = c
            if op == ')':
                break
    return functools.reduce(lambda a,b : a*b, stack)

r = [ev(list(l.strip())) for l in sys.stdin]
print(r)
print(sum(r))