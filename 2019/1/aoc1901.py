import sys

s1,s2 = 0,0
for m in sys.stdin:
    f = int(m)//3-2
    s1 += f
    while f > 0:
        s2 += f
        f = f//3-2
print(s1)
print(s2)
