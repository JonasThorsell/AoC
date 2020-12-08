# Copyright (c) 2020 Jonas Thorsell
import sys

prg=[]
for l in sys.stdin:
    op, arg = l.split(' ')
    arg = int(arg)
    prg.append((op, arg))

acc = 0
ip = 0
mark = set()

while not ip in mark:
    print(f"ip={ip} acc={acc} {prg[ip][0]} {prg[ip][1]}")
    mark |= {ip}
    if prg[ip][0] == 'jmp':
        ip = ip + prg[ip][1] - 1
    elif prg[ip][0] == 'acc':
        acc += prg[ip][1]
    ip += 1

print(acc)
