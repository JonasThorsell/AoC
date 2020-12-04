# Copyright (c) 2020 Jonas Thorsell
import sys
import re

pl=[{}]
for l in sys.stdin:
    if l.strip():
        pl[-1].update({kv.split(':')[0]: kv.split(':')[1] for kv in l.split()})
    else:
        pl.append({})

def chkp(p):
    fl = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    ecl = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if not all(f in p for f in fl):
        return False
    if (not p['byr'].isdigit() or int(p['byr']) < 1920 or int(p['byr']) > 2002):
        return False
    if (not p['iyr'].isdigit() or int(p['iyr']) < 2010 or int(p['iyr']) > 2020):
        return False
    if (not p['eyr'].isdigit() or int(p['eyr']) < 2020 or int(p['eyr']) > 2030):
        return False
    hgtu = p['hgt'][-2:]
    hgtv = p['hgt'][:-2]
    if (not hgtu in ['cm', 'in'] or not hgtv.isdigit()):
        return False
    if (hgtu == 'cm' and (int(hgtv) < 150 or int(hgtv) > 193)):
        return False
    if (hgtu == 'in' and (int(hgtv) < 59 or int(hgtv) > 76)):
        return False
    if (not re.search("^#[0-9a-f]{6}$", p['hcl'])):
        return False
    if (not p['ecl'] in ecl):
        return False
    if (not p['pid'].isdigit() or len(p['pid']) != 9):
        return False
    return True

vpl = list(filter(chkp, pl))
print(len(vpl))
