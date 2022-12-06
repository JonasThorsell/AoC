import sys
for l in sys.stdin:
    n1,n2=0,0
    while(len(set(l[n1:n1+4]))<4):
        n1+=1
    while(len(set(l[n2:n2+14]))<14):
        n2+=1
    print(n1+4, n2+14)
