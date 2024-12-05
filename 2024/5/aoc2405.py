import sys

def inorder(rl, pl):
    for r in rl:
        if r[0] in pl and r[1] in pl:
            if pl.index(r[0]) > pl.index(r[1]):
                return False
    return True

def order(rl, pl):
    while not inorder(rl, pl):
        for r in rl:
            if r[0] in pl and r[1] in pl:
                if (a:=pl.index(r[0])) > (b:=pl.index(r[1])):
                    pl[a],pl[b] = pl[b],pl[a]

rules = []
updates = []
rdone = False
for l in sys.stdin:
    if not l.strip():
        rdone = True
    elif not rdone:
        rules.append(tuple(map(int, l.split('|'))))
    else:
        updates.append(list(map(int, l.split(','))))

s1,s2 = 0,0
for pages in updates:
    if inorder(rules, pages):
        s1 += pages[len(pages)//2]
    else:
        order(rules, pages)
        s2 += pages[len(pages)//2]

print(s1)
print(s2)
