import sys

def next(s):
    if s.count(0) == len(s):
        return 0
    return s[-1] + next([s[i]-s[i-1] for i in range(1,len(s))])

def prev(s):
    if s.count(0) == len(s):
        return 0
    return s[0] - prev([s[i]-s[i-1] for i in range(1,len(s))])

sum1,sum2 = 0,0
for l in sys.stdin:
    seq = [int(x) for x in l.split()]
    sum1 += next(seq)
    sum2 += prev(seq) 
print(sum1)
print(sum2)
