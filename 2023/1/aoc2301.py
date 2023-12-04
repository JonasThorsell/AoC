import sys
nbr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
n1, n2 = 0, 0
for l in sys.stdin:
    l = l.strip()
    a1,b1 = -1,-1
    a2,b2 = -1,-1
    for i in range(len(l)):
        if l[i].isdigit():
            b2 = b1 = int(l[i])
            if a1 < 0:
                a1 = b1
            if a2 < 0:
                a2 = b2
        for v,s in enumerate(nbr):
            if s == l[i:i+len(s)]:
                b2 = v
                if a2 < 0:
                    a2 = b2
    n1 += a1 * 10 + b1
    n2 += a2 * 10 + b2
print(n1)
print(n2)
