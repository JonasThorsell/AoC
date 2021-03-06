# Copyright (c) 2020 Jonas Thorsell
import sys

bags={}
for l in sys.stdin:
    i = l.find(' bags contain ')
    bag = l[:i]
    if bag in bags:
        print(f'Repeated bag type {bag}')
    bags[bag] = {}
    cont = [x[:x.find(' bag')] for x in l[i+14:].split(', ')]
    for c in cont:
        if c == 'no other':
            continue
        j = c.find(' ')
        cnt = int(c[:j])
        tp = c[j+1:]
        bags[bag][tp] = cnt

def lubag(bl, bt):
    n = 1
    for b in bl[bt]:
        n += bl[bt][b] * lubag(bl, b) 
    return n

print(lubag(bags, 'shiny gold') - 1)
