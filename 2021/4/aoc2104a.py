# Copyright (c) 2021 Jonas Thorsell
import sys
import numpy as np

numbers = [int(x) for x in sys.stdin.readline().split(',')]
print(numbers)

board = []
for l in sys.stdin:
    if len(l.strip()) != 0:
        board.append([int(x) for x in l.split()])
board = np.array(board).reshape((-1,5,5))
mark = np.zeros(board.shape, dtype=np.uint)

w = None
for n in numbers:
    mark[board == n] = 1
    if np.any(mark.sum(axis=2) == 5):
        w = (mark.sum(axis=2) == 5).nonzero()[0][0]
        break
    if np.any(mark.sum(axis=1) == 5):
        w = (mark.sum(axis=1) == 5).nonzero()[0][0]
        break

print(w)
print(board[w])
print(mark[w])
s = board[w][mark[w] == 0].sum()
print(f'{s} * {n} = {s*n}')
