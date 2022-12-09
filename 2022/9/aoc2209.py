import sys

r=[(0,0) for i in range(10)]
h1, h2 = [], []

for l in sys.stdin:
    d,n = l.split()
    n=int(n)
    while n>0:
        if d=='R':
            r[0]=(r[0][0]+1,r[0][1])
        if d=='L':
            r[0]=(r[0][0]-1,r[0][1])
        if d=='D':
            r[0]=(r[0][0],r[0][1]-1)
        if d=='U':
            r[0]=(r[0][0],r[0][1]+1)
        for i in range(1,len(r)):
            if (r[i][0]-r[i-1][0])**2+(r[i][1]-r[i-1][1])**2 > 2:    
                if r[i][0] == r[i-1][0]:
                    r[i] = (r[i][0],r[i][1] + (1 if r[i][1] < r[i-1][1] else -1))
                elif r[i][1] == r[i-1][1]:
                    r[i] = (r[i][0] + (1 if r[i][0] < r[i-1][0] else -1),r[i][1])
                else:
                    r[i] = (r[i][0],r[i][1] + (1 if r[i][1] < r[i-1][1] else -1))
                    r[i] = (r[i][0] + (1 if r[i][0] < r[i-1][0] else -1),r[i][1])
        h1.append(r[1])
        h2.append(r[9])
        n-=1

print(len(set(h1)))
print(len(set(h2)))
