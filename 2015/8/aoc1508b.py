# Copyright (c) 2021 Jonas Thorsell
import sys
import re

s1, s2 = 0, 0
for l in sys.stdin:
    s = l.strip()
    d = re.sub(r'\\', r'\\\\', s)
    d = re.sub(r'\"', r'\\"', d)
    d = '"' + d + '"'
    s1 = s1 + len(s)
    s2 = s2 + len(d)

print(f'{s2} - {s1} = {s2-s1}')
