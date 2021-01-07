# Copyright (c) 2021 Jonas Thorsell
import sys

mem = {}
reg = [0] * 8
stack = []
ip = 0
tin = ""
obs = []

def load(path):
    with open(path, "rb") as f:
        word = f.read(2)
        p = 0
        while word:
            v = int.from_bytes(word, byteorder='little', signed=False)
            mem[p] = v
            p += 1
            word = f.read(2)

def getm(p):
    a = mem[p]
    if a <= 32767:
        return a
    elif a <= 32775:
        r = a - 32768
        if r in obs:
            print(f'@ Reading R{r} at {ip-1} ({reg[r]})')
        return reg[r]
    else:
        print('ERROR! Invalid memory {a}')

def setr(p, v):
    a = mem[p]
    if 32768 <= a <= 32775:
        r = a - 32768
        if r in obs:
            print(f'@ Writing R{r} at {ip-1} ({reg[r]} -> {v})')
        reg[r] = v
    else:
        print('ERROR! Not a register {a}')

def m2s(a):
    op = ["halt","set","push","pop","eq","gt","jmp","jt","jf","add","mult","mod","and","or","not","rmem","wmem","call","ret","out","in","noop"]
    if a <= 21:
        return f"{a} {op[a]}"
    elif a <= 32767:
        return f"{a}"
    elif a <= 32775:
        r = a - 32768
        return f"R{r} ({reg[r]})"
    else:
        return "INV"

def dbgcmd(s):
    args = s[1:].strip().split(' ')
    # q: Quit
    if args[0] == 'q':
        return False
    # p: Print status
    elif args[0] == 'p':
        print(f'IP: {ip+1} R: {reg} S: {stack}')
    # m address [length] : Print memory
    if args[0] == 'm':
        a = int(args[1])
        for _ in range(1 if len(args) < 3 else int(args[2])):
            print(f'{a:5}: {m2s(mem[a])}')
            a += 1
    # r register [new value] : Read or set register value
    if args[0] == 'r':
        r = int(args[1])
        if len(args) < 3:
            print(f"R{r} {reg[r]}")
        else:
            v = int(args[2])
            print(f"R{r} {reg[r]} -> {v}")
            reg[r] = v
    # w address [new value] : Read or write memory
    if args[0] == 'w':
        a = int(args[1])
        if len(args) < 3:
            print(f"{a:5}: {m2s(mem[a])}")
        else:
            v = int(args[2])
            print(f"{a:5}: {m2s(mem[a])} -> {m2s(v)}")
            mem[a] = v
    # o register : Observe register for access
    if args[0] == 'o':
        r = int(args[1])
        if r in obs:
            obs.remove(r)
        else:
            obs.append(r)
    return True

def step():
    global ip
    global tin
    op = mem[ip]
    ip += 1
    # halt: 0
    #   stop execution and terminate the program
    if (op == 0):
        print(f'{ip-1} HALT')
        return False
    # set: 1 a b
    #   set register <a> to the value of <b>
    elif (op == 1):
        setr(ip, getm(ip+1))
        ip += 2
    # push: 2 a
    #   push <a> onto the stack
    elif (op == 2):
        stack.append(getm(ip))
        ip += 1
    # pop: 3 a
    #   remove the top element from the stack and write it into <a>; empty stack = error
    elif (op == 3):
        if stack:
            v = stack.pop()
            setr(ip, v)
        else:
            print('ERROR! Stack empty')
            return False
        ip += 1
    # eq: 4 a b c
    #   set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
    elif (op == 4):
        setr(ip, 1 if getm(ip+1) == getm(ip+2) else 0)
        ip += 3
    # gt: 5 a b c
    #   set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise
    elif (op == 5):
        setr(ip, 1 if getm(ip+1) > getm(ip+2) else 0)
        ip += 3
    # jmp: 6 a
    #   jump to <a>
    elif (op == 6):
        ip = getm(ip)
    # jt: 7 a b
    #   if <a> is nonzero, jump to <b>
    elif (op == 7):
        if getm(ip):
            ip = getm(ip+1)
        else:
            ip += 2
    # jf: 8 a b
    #   if <a> is zero, jump to <b>
    elif (op == 8):
        if not getm(ip):
            ip = getm(ip+1)
        else:
            ip += 2
    # add: 9 a b c
    #   assign into <a> the sum of <b> and <c> (modulo 32768)
    elif (op == 9):
        setr(ip, (getm(ip+1) + getm(ip+2)) % 32768)
        ip += 3
    # mult: 10 a b c
    #   store into <a> the product of <b> and <c> (modulo 32768)
    elif (op == 10):
        setr(ip, (getm(ip+1) * getm(ip+2)) % 32768)
        ip += 3
    # mod: 11 a b c
    #   store into <a> the remainder of <b> divided by <c>
    elif (op == 11):
        setr(ip, getm(ip+1) % getm(ip+2))
        ip += 3
    # and: 12 a b c
    #   stores into <a> the bitwise and of <b> and <c>
    elif (op == 12):
        setr(ip, getm(ip+1) & getm(ip+2))
        ip += 3
    # or: 13 a b c
    #   stores into <a> the bitwise or of <b> and <c>
    elif (op == 13):
        setr(ip, getm(ip+1) | getm(ip+2))
        ip += 3
    # not: 14 a b
    #   stores 15-bit bitwise inverse of <b> in <a>
    elif (op == 14):
        setr(ip, (~getm(ip+1)) & 0x7FFF)
        ip += 2
    # rmem: 15 a b
    #   read memory at address <b> and write it to <a>
    elif (op == 15):
        setr(ip, mem[getm(ip+1)])
        ip += 2
    # wmem: 16 a b
    #   write the value from <b> into memory at address <a>
    elif (op == 16):
        mem[getm(ip)] = getm(ip+1)
        ip += 2
    # call: 17 a
    #   write the address of the next instruction to the stack and jump to <a>
    elif (op == 17):
        stack.append(ip+1)
        ip = getm(ip)
    # ret: 18
    #   remove the top element from the stack and jump to it; empty stack = halt
    elif (op == 18):
        if stack:
            ip = stack.pop()
        else:
            print('ERROR! Stack empty')
            return False
    # out: 19 a
    #   write the character represented by ascii code <a> to the terminal
    elif (op == 19): # OUT
        a = chr(getm(ip))
        ip += 1
        print(a, end='')
    # in: 20 a
    #   read a character from the terminal and write its ascii code to <a>;
    #   it can be assumed that once input starts, it will continue until a
    #   newline is encountered; this means that you can safely read whole lines
    #   from the keyboard and trust that they will be fully read
    elif (op == 20):
        if not tin:
            # Ask for input if buffer is empty
            tin = input ("> ")
            tin += '\n'
        if (tin[0] == '!'):
            # '!' used as escape for debug command
            nl = tin.find('\n')
            if not dbgcmd(tin[:nl]):
                return False
            tin = tin[nl:]
        setr(ip, ord(tin[0]))
        tin = tin[1:]
        ip += 1
    # noop: 21
    #   no operation
    elif (op == 21):
        return True
    else:
        print(f'{ip-1} Unsupported opcode {op}')
        return False
    return True

if len(sys.argv) < 2:
    print(f'Usage: {sys.argv[0]} <binary> [Input]')
    quit()

load(sys.argv[1])

if len(sys.argv) >= 3:
    with open(sys.argv[2], "r") as f:
        tin = f.read()

cycle = 0
while (step()):
    cycle += 1

print(f'Done after {cycle} cycles')
