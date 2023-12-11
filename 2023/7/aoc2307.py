import sys
from collections import Counter
from functools import cmp_to_key

strength = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}

def handtype(h):
    cnt = Counter(h)
    if len(cnt) == 1:
        return 6
    if len(cnt) == 2:
        a,b = list(cnt)
        if cnt[a] == 4 or cnt[b] == 4:
            return 5
        return 4
    if len(cnt) == 3:
        a,b,c = list(cnt)
        if cnt[a] == 3 or cnt[b] == 3 or cnt[c] == 3:
            return 3
        return 2
    if len(cnt) == 4:
        return 1
    return 0

def handcmp(a, b):
    ta, tb = handtype(a[0]), handtype(b[0])
    if ta < tb:
        return -1
    if ta > tb:
        return 1
    for i in range(5):
        if strength[a[0][i]] < strength[b[0][i]]:
            return -1
        if strength[a[0][i]] > strength[b[0][i]]:
            return 1
    return 0

hands = []
for l in sys.stdin:
    l = l.split()
    hands.append((l[0], int(l[1])))
hands.sort(key=cmp_to_key(handcmp))
s = 0
for i in range(len(hands)):
    s += (i+1) * hands[i][1]
print(s)
