# Copyright (c) 2021 Jonas Thorsell
import sys

gversum = 0

def decode(s, npkg=-1):
    global gversum
    i = 0
    while len(s) - i >= 6 and npkg != 0:
        version = int(s[i:i+3],2)
        gversum += version
        typeid = int(s[i+3:i+6],2)
        i += 6
        if npkg > 0: npkg -= 1
        #print(version, typeid)
        if typeid == 4: # literal value
            literals = ''
            literal = 0
            group = 1
            while group:
                group = int(s[i])
                i += 1
                literals += s[i:i+4]
                i+=4
            literal = int(literals,2)
            print(version, typeid, literal)
        else: # operator
            lengthtype = int(s[i])
            i += 1
            if lengthtype == 0: # total length in bits
                sublength = int(s[i:i+15],2)
                print(version, typeid, lengthtype, sublength)
                i+=15
                decode(s[i:i+sublength])
                i+=sublength
            else:
                subpkg = int(s[i:i+11],2)
                print(version, typeid, lengthtype, subpkg)
                i+=11
                i+=decode(s[i:], subpkg)
    return i

for l in sys.stdin:
    bits =''
    gversum = 0
    for c in l.strip():
        bits += '{:04b}'.format(int(c,16))
    print(l.strip())
    print(bits)
    decode(bits,1)
    print(gversum)
    i=0

