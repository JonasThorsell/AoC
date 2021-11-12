# Copyright (c) 2021 Jonas Thorsell
import sys

nice = 0
for l in sys.stdin:
    l = l.strip()
    pc, rc = 0, 0
    for i in range(0, len(l)):
        if i < len(l)-3 and l[i:i+2] in l[i+2:]:
            pc=pc+1
        if i < len(l)-2 and l[i] == l[i+2]:
            rc=rc+1
    if pc and rc:
        nice=nice+1

print(nice)
