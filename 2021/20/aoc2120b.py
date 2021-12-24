# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

bc = [2**x for x in range(8,-1,-1)]
key = np.array([1 if c=='#' else 0 for c in sys.stdin.readline().strip()], dtype=np.uint)
sys.stdin.readline()
img = []
for l in sys.stdin:
    img.append([1 if c=='#' else 0 for c in l.strip()])
img = np.array(img, dtype=np.uint)

pv = 0
for l in range(50):
    img = np.pad(img, 2, constant_values=pv)
    nxt = img.copy()
    for y in range(1, img.shape[0]-1):
        for x in range(1,img.shape[1]-1):
            m = img[y-1:y+2,x-1:x+2].reshape((9))
            nxt[y,x] = key[int(np.sum(m*bc))]
    pv = key[0 if img[0,0] == 0 else -1]
    img = nxt[1:-1,1:-1]
print(np.sum(img))
