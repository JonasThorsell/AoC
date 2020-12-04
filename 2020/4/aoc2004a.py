# Copyright (c) 2020 Jonas Thorsell
import sys

pl=[{}]
for l in sys.stdin:
    if l.strip():
        pl[-1].update({kv.split(':')[0]: kv.split(':')[1] for kv in l.split()})
    else:
        pl.append({})

fl = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
vpl = list(filter(lambda p : all(f in p for f in fl), pl))
print(len(vpl))
