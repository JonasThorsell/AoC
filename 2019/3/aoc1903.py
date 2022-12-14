def trace(t):
    s, p = [], (0,0)
    dy = {'U': 1,'D':-1,'R': 0,'L': 0}
    dx = {'U': 0,'D': 0,'R': 1,'L':-1}
    for c in t:
        d, n = c[0], int(c[1:])
        for _ in range(n):
            p = (p[0]+dx[d], p[1]+dy[d])
            s.append(p)
    return s

a=trace(input().split(','))
b=trace(input().split(','))
isec = list(set(a)&set(b))
print(sorted([abs(x)+abs(y) for x,y in isec])[0])
print(sorted([a.index(p)+b.index(p)+2 for p in isec])[0])
