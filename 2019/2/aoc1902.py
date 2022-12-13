
def run(m):
    ip = 0
    while (not m[ip] == 99):
        op = m[ip]
        if op == 1:
            p1,p2,p3 = m[ip+1:ip+4]
            m[p3] = m[p1] + m[p2]
            ip += 4
        elif op == 2:
            p1,p2,p3 = m[ip+1:ip+4]
            m[p3] = m[p1] * m[p2]
            ip += 4
        else:
            raise NotImplementedError('Intcode: Invalid Opcode ' + str(op) + ' @ ' + str(ip))

orgmem = [int(x) for x in input().split(',')]

m = orgmem.copy()
m[1] = 12
m[2] = 2
run(m)
print(m[0])

n,v,o=0,-1,0
while not o == 19690720:
    v += 1
    if v > 99:
        n,v = n+1,0
    m = orgmem.copy()
    m[1],m[2] = n,v
    run(m)
    o = m[0]
print(100*n+v)
