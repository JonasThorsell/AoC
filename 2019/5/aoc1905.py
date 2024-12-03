import sys

def run(m):
    ip = 0
    while (not m[ip] == 99):
        op = m[ip] % 100
        m1 = (m[ip] // 100) % 10
        m2 = (m[ip] // 1000) % 10
        m3 = (m[ip] // 10000) % 10

        # Add
        if op == 1:
            p1,p2,p3 = m[ip+1:ip+4]
            if not m1:
                p1 = m[p1]
            if not m2:
                p2 = m[p2]
            if m3:
                raise NotImplementedError('Intcode: Invalid Mode ' + str(m[ip]) + ' @ ' + str(ip))
            m[p3] = p1 + p2
            ip += 4
        
        # Multipli
        elif op == 2:
            p1,p2,p3 = m[ip+1:ip+4]
            if not m1:
                p1 = m[p1]
            if not m2:
                p2 = m[p2]
            if m3:
                raise NotImplementedError('Intcode: Invalid Mode ' + str(m[ip]) + ' @ ' + str(ip))
            m[p3] = p1 * p2
            ip += 4
        
        # Input
        elif op == 3:
            p1 = m[ip+1]
            if m1:
                raise NotImplementedError('Intcode: Invalid Mode ' + str(m[ip]) + ' @ ' + str(ip))
            m[p1] = int(input())
            ip += 2
        
        # Output
        elif op == 4:
            p1 = m[ip+1]
            if not m1:
                p1 = m[p1]
            print(p1)
            ip += 2

        # Jump if True
        elif op == 5:
            p1,p2 = m[ip+1:ip+3]
            if not m1:
                p1 = m[p1]
            if not m2:
                p2 = m[p2]
            if p1:
                ip = p2
            else:
                ip += 3

        # Jump if False
        elif op == 6:
            p1,p2 = m[ip+1:ip+3]
            if not m1:
                p1 = m[p1]
            if not m2:
                p2 = m[p2]
            if not p1:
                ip = p2
            else:
                ip += 3
        
        # Less than
        elif op == 7:
            p1,p2,p3 = m[ip+1:ip+4]
            if not m1:
                p1 = m[p1]
            if not m2:
                p2 = m[p2]
            if m3:
                raise NotImplementedError('Intcode: Invalid Mode ' + str(m[ip]) + ' @ ' + str(ip))
            m[p3] = p1 < p2
            ip += 4

        # Equals
        elif op == 8:
            p1,p2,p3 = m[ip+1:ip+4]
            if not m1:
                p1 = m[p1]
            if not m2:
                p2 = m[p2]
            if m3:
                raise NotImplementedError('Intcode: Invalid Mode ' + str(m[ip]) + ' @ ' + str(ip))
            m[p3] = p1 == p2
            ip += 4

        else:
            raise NotImplementedError('Intcode: Invalid Opcode ' + str(m[ip]) + ' @ ' + str(ip))

with open(sys.argv[1]) as f:
    orgmem = [int(x) for x in f.read().split(',')]

m = orgmem.copy()
run(m)
