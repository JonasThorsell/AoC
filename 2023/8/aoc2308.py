import sys

steps = input().strip()
input()
nodemap = dict()
for l in sys.stdin:
    n,l,r = l[0:3],l[7:10],l[12:15]
    nodemap[n] = (l,r)

score = 0
node = 'AAA'
i = 0
while not node == 'ZZZ':
    node = nodemap[node][0 if steps[i] == 'L' else 1]
    i = (i+1)%len(steps)
    score += 1
print(score)
