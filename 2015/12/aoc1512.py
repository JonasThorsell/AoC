# Copyright (c) 2022 Jonas Thorsell
import sys
import json

def exnum1(jd):
    if isinstance(jd, dict):
        return sum(map(exnum1, jd.values()))
    if isinstance(jd, list):
        return sum(map(exnum1, jd))
    if isinstance(jd, int):
        return jd
    return 0

def exnum2(jd):
    if isinstance(jd, dict):
        if 'red' in jd.values():
            return 0
        return sum(map(exnum2, jd.values()))
    if isinstance(jd, list):
        return sum(map(exnum2, jd))
    if isinstance(jd, int):
        return jd
    return 0

for l in sys.stdin:
    jd = json.loads(l)
    print(exnum1(jd))
    print(exnum2(jd))
