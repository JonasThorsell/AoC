# Copyright (c) 2020 Jonas Thorsell
import sys

mem={}
m = '0'*36
for l in sys.stdin:
    if (l[:4] == "mask"):
        m = l.split('=')[1].strip()
    else:
        a = int(l.split('=')[0].strip()[4:-1])
        v = int(l.split('=')[1].strip())
        x = m.count('X')
        for i in range(2**x):
            ix = 0
            for j in range(len(m)-1,-1,-1):
                if (m[j] == 'X'):
                    if (i & (1 << ix)):
                        a = a | (1 << (len(m) - j - 1))
                    else:
                        a = a & ~(1 << (len(m) - j - 1))
                    ix += 1
                elif (m[j] == '1'):
                    a = a | (1 << (len(m) - j - 1))
            mem[a] = v

print(sum(mem.values()))
