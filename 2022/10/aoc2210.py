import sys

prg = []
for l in sys.stdin:
    i = l.split()
    if len(i)>1:
        i[1] = int(i[1])
    prg.append(i)

X = 1
c = 0
pc = 0
s=0
ss = 0
while c < 240:
    c += 1
    
    if ((c-20)%40)==0:
        ss += c*X
    
    x = (c-1)%40
    if x>=X-1 and x<=X+1:
        print('#',end='')
    else:
        print('.',end='')
    if x==39:
        print()
    
    if prg[pc][0] == 'addx':
        s -= 1
        if s == -1:
            s = 1
        if s == 0:
            X += prg[pc][1]
            pc = (pc+1) % len(prg)
    else:
        pc = (pc+1) % len(prg)

print(ss)

