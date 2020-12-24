# Copyright (c) 2020 Jonas Thorsell
import sys

def s2c(s):
    x, y = 0, 0
    p = ''
    for c in s:
        if c == 'n' or c == 's':
            p = c
        elif c == 'e':
            if p == 'n':
                if (y % 2) == 1:
                    x += 1
                y -= 1
            elif p == 's':
                if (y % 2) == 1:
                    x += 1
                y += 1
            else:
                x += 1
            p = ''
        elif c == 'w':
            if p == 'n':
                if (y % 2) == 0:
                    x -= 1
                y -= 1
            elif p == 's':
                if (y % 2) == 0:
                    x -= 1
                y += 1
            else:
                x -= 1
            p = ''
        else:
            print('Bork!')
    return (x,y)

t = {}
for l in sys.stdin:
    c = s2c(l.strip())
    if c in t:
        t[c] = not t[c]
    else:
        t[c] = True

print(list(t.values()).count(True))
