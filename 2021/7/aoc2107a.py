# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

cp = np.array(sorted([int(x) for x in sys.stdin.readline().split(',')]))
f = [np.sum(np.abs(cp - p)) for p in range(cp[0], cp[-1]+1)]
print(min(f))
