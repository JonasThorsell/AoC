# Copyright (c) 2020 Jonas Thorsell
import sys

food=[]
for l in sys.stdin:
    ing, alg = l.strip().split(" (contains ")
    ing = ing.split(' ')
    alg = alg[:-1].split(', ')
    food.append([ing, alg])

a2i = {}
for ing, alg in food:
    for a in alg:
        if not a in a2i:
            a2i[a] = set(ing)
        else:
            a2i[a] &= set(ing)

again = True
while again:
    again = False
    for a in a2i:
        if len(a2i[a]) == 1:
            i = next(iter(a2i[a]))
            for aa in a2i:
                if len(a2i[aa]) > 1 and i in a2i[aa]:
                    a2i[aa].remove(i)
                    again = True

dai = sorted([(a,next(iter(a2i[a]))) for a in a2i])
di = [ai[1] for ai in dai]
print(",".join(di))
