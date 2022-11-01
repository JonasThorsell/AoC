# Copyright (c) 2022 Jonas Thorsell
import sys

a = sys.stdin.readline().strip()
print(a)
for cnt in range(50):
    i = 0
    b = ''
    while i < len(a):
        d = a[i]
        c = 1
        while i+c < len(a) and a[i+c] == d:
            c += 1
        b += str(c) + str(d)
        i += c
    a = b
    print(cnt+1)
print(len(a))
