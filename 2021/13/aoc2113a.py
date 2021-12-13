# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

dots, folds = [], []

for l in sys.stdin:
    if not l.strip(): break
    x,y = l.strip().split(',')
    dots.append((int(x),int(y)))

for l in sys.stdin:
    a,n=l.split()[2].split('=')
    folds.append((a,int(n)))

w = 2 * sorted([x[1] for x in folds if x[0]=='x'])[-1] + 1
h = 2 * sorted([y[1] for y in folds if y[0]=='y'])[-1] + 1
page = np.zeros((w,h),dtype=np.uint)
for x,y in dots:
    page[x,y] = 1

a,n = folds[0]
if a=='x': page = page[0:n,:]+page[-1:n:-1,:]
if a=='y': page = page[:,0:n]+page[:,-1:n:-1]

print(np.sum(np.clip(page,None,1)))
