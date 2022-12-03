import sys
s1 = 0
s2 = 0
g = []
for l in sys.stdin:
    l = l.strip()
    # Part Two
    g.append(l)
    if len(g) == 3:
        t = set(g[0]) & set(g[1]) & set(g[2])
        c = ord(t.pop())
        p = c - (96 if c > 96 else 38)
        s2 += p
        g = []
    # Part One
    n = len(l)
    t = set(l[:n//2]) & set(l[n//2:])
    c = ord(t.pop())
    p = c - (96 if c > 96 else 38)
    s1 += p
print(s1)
print(s2)
