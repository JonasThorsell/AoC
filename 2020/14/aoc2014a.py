# Copyright (c) 2020 Jonas Thorsell
import sys

sm, cm = 0, int('1'*36, 2)
mem={}
for l in sys.stdin:
    if (l[:4] == "mask"):
        sm, cm = 0, int('1'*36, 2)
        m = l.split('=')[1].strip()
        for i in range(len(m)):
            if (m[i] == '1'):
                sm = sm | (1 << (len(m) - i - 1))
            elif (m[i] == '0'):
                cm = cm & ~(1 << (len(m) - i - 1))
    else:
        a = int(l.split('=')[0].strip()[4:-1])
        v = int(l.split('=')[1].strip())
        mv = (v | sm) & cm
        mem[a] = mv

print(sum(mem.values()))
