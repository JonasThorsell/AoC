jet = [-1 if x=='<' else 1 for x in input().strip()]
jeti=0

chamber = [[0]*7 for _ in range(3)]
shapes=\
    [[[1,1,1,1]],\
    [[0,1,0],[1,1,1],[0,1,0]],\
    [[0,0,1],[0,0,1],[1,1,1]],\
    [[1],[1],[1],[1]],\
    [[1,1],[1,1]]]
rocks=0
tall=0
si=0
sx,sy=0,-1
sh,sw=0,0

def pchamb(c):
    for l in chamber:
        print('|',end='')
        for c in l:
            print('#' if c else ' ',end='')
        print('|')
    print('+-------+')

while rocks<2022:
    if sy==-1:
        sh=len(shapes[si])
        sw=len(shapes[si][0])
        while len(chamber) < tall+3+sh:
            chamber.insert(0,[0]*7)
        sx=2
        sy=len(chamber)-tall-3-sh
    jd = jet[jeti]
    jeti=(jeti+1)%len(jet)
    jp=True
    if sx+jd>=0 and sx+sw+jd<=7:
        for x in range(sw):
            for y in range(sh):
                if shapes[si][y][x] and chamber[sy+y][sx+x+jd]:
                    jp=False
        if jp:
            sx+=jd
    gp=True
    if sy+1<len(chamber):
        for x in range(sw):
            for y in range(sh):
                if shapes[si][y][x] and chamber[sy+y+1][sx+x]:
                    gp=False
    else:
        gp=False
    if gp:
        sy+=1
    else:
        for x in range(sw):
            for y in range(sh):
                if shapes[si][y][x]:
                    chamber[sy+y][sx+x]=1
        rocks += 1
        tall = max(tall,len(chamber)-sy)
        sy = -1
        si = (si+1)%5
        #pchamb(chamber)
        #print(rocks,tall)

print(f'After {rocks} rocks the tower height is {tall}')
