# Copyright (c) 2020 Jonas Thorsell
import sys
import re

def chktf(tf, tfr):
    for r in tfr:
        if (r[1] <= tf <= r[2] or r[3] <= tf <= r[4]):
            return True
    return False


p = re.compile(r'^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)')
tfr=[]
for l in sys.stdin:
    if not l.strip():
        break
    tfr.append([int(x) if x.isdigit() else x for x in p.match(l).groups()])

sys.stdin.readline()
mt = [int(x) for x in sys.stdin.readline().split(',')]

sys.stdin.readline()
sys.stdin.readline()
nt = []
for l in sys.stdin:
    nt.append([int(x) for x in l.split(',')])

ivf = [f for t in nt for f in t if not chktf(f, tfr)]
print(sum(ivf))
