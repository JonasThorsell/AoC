import sys
a,b = [], []
for l in sys.stdin:
    sa, sb = l.split()
    a.append(int(sa))
    b.append(int(sb))
d1 = [abs(x-y) for x,y in zip(sorted(a),sorted(b))]
print(sum(d1))
d2 = [x*b.count(x) for x in a]
print(sum(d2))
