# Copyright (c) 2020 Jonas Thorsell
import sys
import re
import functools

def chktf(tf, tfr):
    for r in tfr:
        if (r[1] <= tf <= r[2] or r[3] <= tf <= r[4]):
            return True
    return False

def matchtfl(tfl, r):
    for f in tfl:
        if not (r[1] <= f <= r[2] or r[3] <= f <= r[4]):
            return False
    return True
        

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

nvt = [t for t in nt if sum([chktf(f, tfr) for f in t]) == len(t)]

gbf = []
for i in range(len(nvt[0])):
    gbf.append([t[i] for t in nvt])

vr = [[] for i in range(len(gbf))]
for r in tfr:
    for i, f in enumerate(gbf):
        if matchtfl(f, r):
            vr[i].append(r[0])

om = [x[0] for x in vr if len(x) == 1]
while (len(om) < len(tfr)):
    for m in om:
        for f in vr:
            if len(f) > 1 and m in f:
                f.remove(m)
    om = [x[0] for x in vr if len(x) == 1]

print(functools.reduce(lambda a,b : a*b, [x[1] for x in zip(om,mt) if x[0][:9] == 'departure']))
