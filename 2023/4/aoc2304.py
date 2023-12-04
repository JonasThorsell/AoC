import sys

cards = []
for l in sys.stdin:
    id, numbers = l.strip().split(':')
    id = int(''.join(id[4:]))
    win,num = numbers.split('|')
    win = [int(x) for x in win.split()]
    num = [int(x) for x in num.split()]
    cards.append([set(win), num, -1])

s1 = 0
for c in cards:
    c[2] = len([x for x in c[1] if x in c[0]])
    s1 += (0 if not c[2] else 2**(c[2]-1))
print(s1)

inst = [0]*len(cards)
def cnt(i):
    inst[i] += 1
    if cards[i][2]:
        for w in range(i+1,min(i+cards[i][2]+1,len(cards))):
            cnt(w)
for i in range(len(cards)):
    cnt(i)
s2 = sum(inst)
print(s2)
