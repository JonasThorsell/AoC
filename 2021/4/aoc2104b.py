# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np
from numpy.core.numeric import count_nonzero

numbers = [int(x) for x in sys.stdin.readline().split(',')]
print(numbers)

board = []
for l in sys.stdin:
    if len(l.strip()) != 0:
        board.append([int(x) for x in l.split()])
board = np.array(board).reshape((-1,5,5))
mark = np.zeros(board.shape, dtype=np.uint)

l = None
w = np.zeros(board.shape[0], dtype=np.uint)
for n in numbers:
    if np.count_nonzero(w) == len(w) - 1:
        l = np.nonzero(w == 0)[0][0]
    mark[board == n] = 1
    if np.any(mark.sum(axis=2) == 5):
        w[(mark.sum(axis=2) == 5).nonzero()[0]] = 1
    if np.any(mark.sum(axis=1) == 5):
        w[(mark.sum(axis=1) == 5).nonzero()[0]] = 1
    if np.count_nonzero(w) == len(w):
        break

print(l)
print(board[l])
print(mark[l])
s = board[l][mark[l] == 0].sum()
print(f'{s} * {n} = {s*n}')
