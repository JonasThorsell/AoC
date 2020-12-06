# Copyright (c) 2020 Jonas Thorsell
import sys

ql=[None]
for l in sys.stdin:
    if l.strip():
        if ql[-1] is not None:
            ql[-1] &= set(list(l.strip()))
        else:
            ql[-1] = set(list(l.strip()))

    else:
        ql.append(None)

print(sum([len(x) for x in ql]))
