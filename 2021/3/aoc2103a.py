# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

d = []
for l in sys.stdin:
    d = d + [[int(x) for x in l.strip()]]
d = np.array(d)
cs = np.sum(d, axis=0)

gb = cs > (d.shape[0]/2)
eb = cs < (d.shape[0]/2)
gd = int(''.join([str(int(x)) for x in gb]), 2)
ed = int(''.join([str(int(x)) for x in eb]), 2)

print(f'{gd} * {ed} = {gd*ed}')
