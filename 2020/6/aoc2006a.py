# Copyright (c) 2020 Jonas Thorsell
import sys

ql=[set()]
for l in sys.stdin:
    if l.strip():
        ql[-1] |= set(list(l.strip()))
    else:
        ql.append(set())

print(sum([len(x) for x in ql]))
