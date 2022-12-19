import sys

bpl=[]
for l in sys.stdin:
    l=l.split()
    bpl.append({'ro_o':int(l[6]),'rc_o':int(l[12]),'rb_o':int(l[18]),'rb_c':int(l[21]),'rg_o':int(l[27]),'rg_b':int(l[30])})

def runbf(bp,s):
    if s['t']+1 == 24:
        return s['ig'] + s['rg']

    max_geo=0

    if s['ib'] >= bp['rg_b'] and s['io'] >= bp['rg_o']:
        sc=s.copy()
        sc['t']+=1
        sc['io'] += s['ro'] - bp['rg_o']
        sc['ic'] += s['rc']
        sc['ib'] += s['rb'] - bp['rg_b']
        sc['ig'] += s['rg']
        sc['rg'] += 1
        return runbf(bp,sc)

    
    if s['ic'] >= bp['rb_c'] and s['io'] >= bp['rb_o']:
        sc=s.copy()
        sc['t']+=1
        sc['io'] += s['ro'] - bp['rb_o']
        sc['ic'] += s['rc'] - bp['rb_c']
        sc['ib'] += s['rb']
        sc['ig'] += s['rg']
        sc['rb'] += 1
        max_geo = max(runbf(bp,sc), max_geo)

    if s['io'] >= bp['rc_o']:
        sc=s.copy()
        sc['t']+=1
        sc['io'] += s['ro'] - bp['rc_o']
        sc['ic'] += s['rc']
        sc['ib'] += s['rb']
        sc['ig'] += s['rg']
        sc['rc'] += 1
        max_geo = max(runbf(bp,sc), max_geo)
    
    if s['io'] >= bp['ro_o']:
        sc=s.copy()
        sc['t']+=1
        sc['io'] += s['ro'] - bp['ro_o']
        sc['ic'] += s['rc']
        sc['ib'] += s['rb']
        sc['ig'] += s['rg']
        sc['ro'] += 1
        max_geo = max(runbf(bp,sc), max_geo)

    if s['io'] < bp['rc_o'] or \
        (s['rc']>0 and(s['io'] < bp['rb_o'] or s['ic'] < bp['rb_c'])) or \
        (s['rb']>0 and (s['io'] < bp['rg_o'] or s['ib'] < bp['rg_b'])):
        sc=s.copy()
        sc['t']+=1
        sc['io'] += s['ro']
        sc['ic'] += s['rc']
        sc['ib'] += s['rb']
        sc['ig'] += s['rg']
        max_geo = max(runbf(bp,sc), max_geo)

    return max_geo


p=[]
for bp in bpl:
    mgeo = runbf(bp, {'t':0,'ro':1,'rc':0,'rb':0,'rg':0,'io':0,'ic':0,'ib':0,'ig':0})
    p.append(mgeo)
    print(f'Blueprint {len(p)} opened {mgeo} geodes')

ql=0
for i in range(len(p)):
    ql+=(i+1)*p[i]
print(ql)
