import sys

def chkspr(rec, grp):
    sr = ''.join(rec).split('.')
    sr = [x for x in sr if x]
    if not len(sr) == len(grp):
        return False
    for r,g in zip(sr, grp):
        if not len(r) == g:
            return False
    return True

s1 = 0
for l in sys.stdin:
    cr, cg = l.split()
    cr = list(cr)
    cg = [int(x) for x in cg.split(',')]
    cq = cr.count('?')
    a = 0
    for p in range(2**cq):
        ptrn = list(f'{p:b}')
        while len(ptrn) < cq:
            ptrn.insert(0,'0')
        rec = [x if not x == '?' else '.' if ptrn.pop() == '1' else '#' for x in cr]
        if chkspr(rec, cg):
            a += 1
    s1 += a
    print(''.join(cr), cg, a)
print(s1)