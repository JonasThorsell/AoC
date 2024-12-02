import sys

def safe(r):
    d = [l1-l0 for l0,l1 in zip(r[0::],r[1::])]
    if len(set([(x>0)-(x<0) for x in d]))==1 and max(d)<=3 and min(d)>=-3 and d.count(0)==0:
        return True
    else:
        return False

s1,s2 = 0,0
for l in sys.stdin:
    r = [int(x) for x in l.split()]
    if safe(r):
        s1 += 1
        s2 += 1
    else:
        for x in range(len(r)):
            if safe(r[0:x]+r[x+1:]):
                s2+=1
                break
print(s1)
print(s2)
