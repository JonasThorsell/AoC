from functools import cmp_to_key

def pkcmp(l,r):
    if isinstance(l, int) and isinstance(r, int):
        return (l > r) - (l < r)
    if isinstance(l, int) and isinstance(r, list):
        l = [l]
    if isinstance(l, list) and isinstance(r, int):
        r = [r]
    if isinstance(l, list) and isinstance(r, list):
        j = 0
        while True:
            if j < len(r) and j>= len(l):
                return -1
            if j < len(l) and j>= len(r):
                return 1
            if j >= len(l) and j>= len(r):
                return 0
            c = pkcmp(l[j], r[j])
            if not c == 0:
                return c
            j += 1
    return 0

cont = True
s = 0
i = 0
pkgs = [[[2]],[[6]]]
while cont:
    i += 1
    l = eval(input().strip())
    r = eval(input().strip())
    pkgs.append(l)
    pkgs.append(r)
    if (pkcmp(l,r)<=0):
        s += i
    try:
        input()
    except EOFError:
        cont = False

print(s)

pkgs = sorted(pkgs, key=cmp_to_key(pkcmp))
d1i = pkgs.index([[2]])+1
d2i = pkgs.index([[6]])+1
print(d1i*d2i)
