import sys


map = []
for l in sys.stdin:
    map.append(list(l.strip()))


def nsym(mr,mc):
    for y in range(max(mr-1,0), min(mr+2, len(map))):
        for x in range(max(mc-1,0), min(mc+2, len(map[0]))):
            if not map[y][x].isdigit() and not map[y][x] == '.':
                return True
    return False


def rpn(r0,c0):
    if r0<0 or r0>=len(map) or c0<0 or c0>=len(map[0]) or not map[r0][c0].isdigit():
        return 0
    while c0>0 and map[r0][c0-1].isdigit():
        c0 -= 1
    c1 = c0
    while c1<len(map[0])-1 and map[r0][c1+1].isdigit():
        c1 += 1
    return int(''.join(map[r0][c0:c1+1]))


s1, sd, pn = 0, False, 0
for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c].isdigit():
            pn = pn * 10 + int(map[r][c])
            sd = sd or nsym(r, c)
            if c == len(map[r])-1 or not map[r][c+1].isdigit():
                if sd:
                    s1 += pn
                sd, pn = False, 0
        else:
            sd, pn = False, 0
print(s1)

s2 = 0
for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] == '*':
            pnl = [rpn(r-1,c-1),rpn(r-1,c),rpn(r-1,c+1),rpn(r,c-1),rpn(r,c+1),rpn(r+1,c-1),rpn(r+1,c),rpn(r+1,c+1)]
            if pnl[1]:
                pnl[0] = pnl[2] = 0
            if pnl[6]:
                pnl[5] = pnl[7] = 0
            pnl = [x for x in pnl if x]
            if len(pnl) == 2:
                s2 += pnl[0]*pnl[1]
print(s2)
