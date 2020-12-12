# Copyright (c) 2020 Jonas Thorsell
import sys

n=[]
for l in sys.stdin:
    n.append((l[0], int(l[1:])))

x, y = 0, 0
f = 90

for i in n:
    if (i[0] == 'N'):
        y += i[1]
    elif (i[0] == 'S'):
        y -= i[1]
    elif (i[0] == 'E'):
        x += i[1]
    elif (i[0] == 'W'):
        x -= i[1]
    elif (i[0] == 'L'):
        f = (f - i[1]) % 360
    elif (i[0] == 'R'):
        f = (f + i[1]) % 360
    elif (i[0] == 'F'):
        if (f == 0):
            y += i[1]
        elif (f == 180):
            y -= i[1]
        elif (f == 90):
            x += i[1]
        elif (f == 270):
            x -= i[1]
        else:
            print(f"Unaligned facing {f}")
    else:
        print(f"Unknown instruction {i[0]}")

print(f"Dist {x},{y} = {abs(x)+abs(y)}")
