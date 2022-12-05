import sys
import copy
m=[]
for l in sys.stdin:
    if not l.strip():
        break
    m.append(l)
w = int(m[-1].split()[-1])
h = len(m)-1
s1 = [ [] for i in range(w)]
s2 = [ [] for i in range(w)]
for i in range(w):
    for j in range(h-1,-1,-1):
        if m[j][4*i+1].isalpha():
            s1[i].append(m[j][4*i+1])
            s2[i].append(m[j][4*i+1])

for l in sys.stdin:
    o = l.split()
    n,f,t = int(o[1]),int(o[3])-1,int(o[5])-1
    for i in range(n):
        s1[t].append(s1[f].pop())
    s2[t].extend(s2[f][-n:])
    s2[f]=s2[f][:-n]

msg1,msg2 = [],[]
for i in range(w):
    msg1.append(s1[i][-1])
    msg2.append(s2[i][-1])
print(''.join(msg1))
print(''.join(msg2))
