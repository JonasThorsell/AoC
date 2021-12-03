# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

def f(a, t):
    a = np.array(a)
    i = 0
    while a.shape[0] > 1:
        cs = np.sum(a, axis=0)
        if cs[i] >= (a.shape[0]/2):
            a = a[a[:,i] == t]
        else:
            a = a[a[:,i] == (not t)]
        i=i+1
    ad = int(''.join([str(int(x)) for x in a[0]]), 2)
    return ad

d = []
for l in sys.stdin:
    d = d + [[int(x) for x in l.strip()]]

od = f(d, True)
cd = f(d, False)

print(f'{od} * {cd} = {od*cd}')
