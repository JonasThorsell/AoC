import sys
v1 = {'AX':4, 'AY':8, 'AZ':3, 'BX':1, 'BY':5, 'BZ':9, 'CX':7, 'CY':2, 'CZ':6}
v2 = {'AX':3, 'AY':4, 'AZ':8, 'BX':1, 'BY':5, 'BZ':9, 'CX':2, 'CY':6, 'CZ':7}
s1,s2 = 0,0
for l in sys.stdin:
    l = l[0]+l[2]
    s1 += v1[l]
    s2 += v2[l]
print(s1)
print(s2)
