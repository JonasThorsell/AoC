# Copyright (c) 2022 Jonas Thorsell
import sys

def pwinc(pw):
    # Rolower ending z to a
    n = len(pw)-1
    while(n >= 0 and pw[n] == 'z'):
        pw[n] = 'a'
        n -= 1
    
    # Increment previous letter
    pw[n] = chr(ord(pw[n])+1)

    # Skipp any i, o, or l
    if 'i' in pw or 'o' in pw or 'l' in pw:
        n = 0
        while not pw[n] in ['i', 'o', 'l']:
            n += 1
        pw[n] = chr(ord(pw[n])+1)
        n += 1
        while n < len(pw):
            pw[n] = 'a'
            n += 1

    return pw

def pwchk(pw):
    # Must be exactly eight letters
    if not len(pw) == 8:
        return False

    # Must include one increasing straight of at least three letters
    ck = False
    for i in range(6):
        if (ord(pw[i])+2) == (ord(pw[i+1])+1) == (ord(pw[i+2])):
            ck = True
    if not ck:
        return False

    # May not contain the letters i, o, or l
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False

    # Must contain at least two different, non-overlapping pairs of letters
    ck = 0
    i = 0
    while i < len(pw)-1:
        if pw[i] == pw[i+1]:
            ck += 1
            i += 1
        i += 1
    if ck < 2:
        return False

    return True

for l in sys.stdin:
    start = list(l.strip())
    
    print(''.join(start), pwchk(start))
    
    pw = pwinc(start)
    while not pwchk(pw):
        pw = pwinc(pw)
    print(''.join(pw))
    
    pw = pwinc(start)
    while not pwchk(pw):
        pw = pwinc(pw)
    print(''.join(pw))
