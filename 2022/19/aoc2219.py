import sys

bpl=[]
for l in sys.stdin:
    l=l.split()
    bpl.append({'ro_o':int(l[6]),'rc_o':int(l[12]),'rb_o':int(l[18]),'rb_c':int(l[21]),'rg_o':int(l[27]),'rg_b':int(l[30])})

def runbf(bp,s={'t':0,'ro':1,'rc':0,'rb':0,'rg':0,'io':0,'ic':0,'ib':0,'ig':0}):
    s[t]+=1
    bro,brc,brb,brg = 0,0,0,0
    if s['ib']>=bp['rg_b'] and s['io']>=bp['rg_o']:
        brg += 1
        s['ib'] -= bp['rg_b']
        s['io'] -= bp['rg_o']
    elif no>=bp[0] and ocr<t[0]:
        bocr += 1
        no   -= bp[0]
    elif no>=bp[1] and ccr<t[1]:
        bccr += 1
        no   -= bp[1]
    elif nc>=bp[3] and no>=bp[2] and obcr<t[2]:
        bobcr += 1
        nc    -= bp[3]
        no    -= bp[2]


    ocr,ccr,obcr,geor = 1,0,0,0
    no,nc,nob,ngeo = 0,0,0,0
    for m in range(24):
        if nob>=bp[5] and no>=bp[4]:
            bgeor += 1
            nob   -= bp[5]
            no    -= bp[4]
        elif no>=bp[0] and ocr<t[0]:
            bocr += 1
            no   -= bp[0]
        elif no>=bp[1] and ccr<t[1]:
            bccr += 1
            no   -= bp[1]
        elif nc>=bp[3] and no>=bp[2] and obcr<t[2]:
            bobcr += 1
            nc    -= bp[3]
            no    -= bp[2]
        no += ocr
        nc += ccr
        nob += obcr
        ngeo += geor
        ocr += bocr
        ccr += bccr
        obcr += bobcr
        geor += bgeor
        bocr,bccr,bobcr,bgeor = 0,0,0,0
        #print(m+1,ocr,no,ccr,nc,obcr,nob,geor,ngeo)
    return ngeo

def runbp(bp,t):
    ocr,ccr,obcr,geor = 1,0,0,0
    no,nc,nob,ngeo = 0,0,0,0
    bocr,bccr,bobcr,bgeor = 0,0,0,0
    for m in range(24):
        if nob>=bp[5] and no>=bp[4]:
            bgeor += 1
            nob   -= bp[5]
            no    -= bp[4]
        elif no>=bp[0] and ocr<t[0]:
            bocr += 1
            no   -= bp[0]
        elif no>=bp[1] and ccr<t[1]:
            bccr += 1
            no   -= bp[1]
        elif nc>=bp[3] and no>=bp[2] and obcr<t[2]:
            bobcr += 1
            nc    -= bp[3]
            no    -= bp[2]
        no += ocr
        nc += ccr
        nob += obcr
        ngeo += geor
        ocr += bocr
        ccr += bccr
        obcr += bobcr
        geor += bgeor
        bocr,bccr,bobcr,bgeor = 0,0,0,0
        #print(m+1,ocr,no,ccr,nc,obcr,nob,geor,ngeo)
    return ngeo

p=[]
for bp in bpl:
    mgeo=0
    t=[1,1,1]
    for x in range(1,9):
        for y in range(1,9):
            for z in range(1,9):
                ngeo=runbp(bp,[x,y,z])
                if runbp(bp,[x,y,z]) > mgeo:
                    mgeo=ngeo
                    t=[x,y,z]
    p.append(mgeo)
    print(f'Blueprint {len(p)} opened {mgeo} geodes using strategy {t}')
