# Copyright (c) 2021 Jonas Thorsell
# 241930482683 too low
import sys
import numpy as np

gversum = 0

def decode(s, ind=0):
    global gversum
    i = 0
    value = 0
    version = int(s[i:i+3],2)
    i += 3
    gversum += version
    typeid = int(s[i:i+3],2)
    i += 3
    if typeid == 4: # literal value
        literals = ''
        literal = 0
        group = 1
        while group == 1:
            group = int(s[i])
            i += 1
            literals += s[i:i+4]
            i+=4
        if group != 0:
            assert False, "Unknown group ID: " + group
        literal = int(literals,2)
        value = literal
        print(f"{'.'*ind}PKG v{version} literal {value}")
    else: # operator
        lengthtype = int(s[i])
        i += 1
        subs = 0
        values = []
        if lengthtype == 0: # total length in bits
            subs = int(s[i:i+15],2)
            i+=15
            j = 0
            while j < subs:
                value, si = decode(s[i:], ind+1)
                values.append(value)
                i += si
                j += si
        elif lengthtype == 1:
            subs = int(s[i:i+11],2)
            i+=11
            j = 0
            while j < subs:
                value, si = decode(s[i:], ind+1)
                values.append(value)
                i += si
                j += 1
        else:
            assert False, 'Unknown length type ID: ' + lengthtype
        if typeid == 0: # sum
            value = np.sum(values)
            print(f'{"."*ind}PKG v{version} {subs}{"p" if lengthtype == 1 else "b"} op sum {values} -> {value}')
        elif typeid == 1: # product
            value = np.prod(values)
            print(f'{"."*ind}PKG v{version} {subs}{"p" if lengthtype == 1 else "b"} op prod {values} -> {value}')
        elif typeid == 2: # minimum
            value = np.amin(values)
            print(f'{"."*ind}PKG v{version} {subs}{"p" if lengthtype == 1 else "b"} op min {values} -> {value}')
        elif typeid == 3: # maximum
            value = np.amax(values)
            print(f'{"."*ind}PKG v{version} {subs}{"p" if lengthtype == 1 else "b"} op max {values} -> {value}')
        elif typeid == 5: # greater than
            assert len(values) == 2
            value = 1 if values[0] > values[1] else 0
            print(f'{"."*ind}PKG v{version} {subs}{"p" if lengthtype == 1 else "b"} op greater {values} -> {value}')
        elif typeid == 6: # less than
            assert len(values) == 2
            value = 1 if values[0] < values[1] else 0
            print(f'{"."*ind}PKG v{version} {subs}{"p" if lengthtype == 1 else "b"} op less {values} -> {value}')
        elif typeid == 7: # equal
            assert len(values) == 2
            value = 1 if values[0] == values[1] else 0
            print(f'{"."*ind}PKG v{version} {subs}{"p" if lengthtype == 1 else "b"} op equal {values} -> {value}')
        else:
            assert False, 'Unknown operator type ID: ' + typeid
    return value, i

for l in sys.stdin:
    bits =''
    gversum = 0
    for c in l.strip():
        bits += '{:04b}'.format(int(c,16))
    print(l.strip())
    print(bits)
    ti = len(bits)
    value, vi = decode(bits)
    print(f'bits {ti}, used {vi}, unused {ti-vi}')
    print(f'>>P1 Version sum : {gversum}')
    print(f'>>P2 Exp value   : {value}')
    i=0

