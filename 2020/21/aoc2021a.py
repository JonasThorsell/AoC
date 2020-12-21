# Copyright (c) 2020 Jonas Thorsell
import sys

food=[]
for l in sys.stdin:
    ing, alg = l.strip().split(" (contains ")
    ing = ing.split(' ')
    alg = alg[:-1].split(', ')
    food.append([ing, alg])

alling = set()
a2i = {}
for ing, alg in food:
    alling.update(ing)
    for a in alg:
        if not a in a2i:
            a2i[a] = set(ing)
        else:
            a2i[a] &= set(ing)

noa = alling.copy()
for pa in a2i:
    noa -= set(a2i[pa])

print(a2i)

cnt = 0
for i in noa:
    for ing, _ in food:
        cnt += ing.count(i)
print(cnt)
