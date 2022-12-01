import sys
e = [0]
i = 0
for l in sys.stdin:
    if l.strip():
        e[i] += int(l)
    else:
        i += 1
        e.append(0)
e=sorted(e, reverse=True)
print(e[0])
print(sum(e[:3]))
