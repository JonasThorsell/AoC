# Copyright (c) 2020 Jonas Thorsell
import sys

prg=[]
for l in sys.stdin:
    op, arg = l.split(' ')
    arg = int(arg)
    prg.append((op, arg))


def test(prg, ip, acc, mark = set(), mcnt = 0):
    while (not ip in mark) and (0 <= ip < len(prg)):
        mark |= {ip}
        if prg[ip][0] == 'jmp':
            if (mcnt == 0):
                rte, rteacc = test(prg, ip+1, acc, mark.copy(), mcnt+1)
                if (rte):
                    print(f"At {ip} change jmp to nop")
                    return (rte, rteacc)
            ip = ip + prg[ip][1] - 1
        elif prg[ip][0] == 'acc':
            acc += prg[ip][1]
        else:
            if (mcnt == 0):
                rte, rteacc = test(prg, ip+prg[ip][1]-1, acc, mark.copy(), mcnt+1)
                if (rte):
                    print(f"At {ip} change nop to jmp")
                    return (rte, rteacc)
        ip += 1
    return (ip == len(prg), acc)


print(test(prg, 0, 0))
