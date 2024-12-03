import sys
import re

s1,s2 = 0,0
e = True
p = re.compile('mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
for l in sys.stdin:
    il = p.findall(l)
    for i in il:
        if i[:3] == 'do(':
            e = True
        elif i[:6] == 'don\'t(':
            e = False
        elif i[:4] == 'mul(':
            a,b = map(int, i[4:-1].split(','))
            s1 += a*b
            if e:
                s2 += a*b
        else:
            raise NotImplementedError('Bad match: ' + i)

print(s1)
print(s2)
