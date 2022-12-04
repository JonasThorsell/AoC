import sys
import re
s1,s2 = 0,0
for l in sys.stdin:
    a0,a1,b0,b1 = [int(x) for x in re.findall(r'\d+', l)]
    if (a0>=b0 and a1<=b1) or (b0>=a0 and b1<=a1):
        s1+=1
    if a1>=b0 and a0<=b1: 
        s2+=1
print(s1)
print(s2)
