# Copyright (c) 2021 Jonas Thorsell
import sys
import itertools
import hashlib

for key in sys.stdin:
    key = key.strip()
    for n in itertools.count(start=1):
        s = key + str(n)
        md5 = hashlib.md5(s).hexdigest()
        if md5[:5] == "00000":
            print(n)
            print("(s: " + key + str(n) + "\tmd5: " + md5 + ")")
            break
