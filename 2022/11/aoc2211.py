import sys

class Monkey:
    nr = 0
    items = []
    op = ''
    oparg = 0
    tst = 0
    tst_true = 0
    tst_false = 0
    cnt_in = 0

    def __init__(self):
        self.nr = int(input().split()[1][:-1])
        self.items = [int(x) for x in input().strip()[15:].split(',')]
        x = input().split()
        self.op = x[4]
        self.oparg = x[5]
        self.tst = int(input().split()[3])
        self.tst_true = int(input().split()[5])
        self.tst_false = int(input().split()[5])

    def __str__(self):
        return f"Monkey {self.nr} inspected items {self.cnt_in} times.\t{self.items}"


ml = []
cont=True
while cont:
    try:
        ml.append(Monkey())
        input()
    except EOFError:
        cont = False

for r in range(20):
    for i in range(len(ml)):
        while ml[i].items:
            w = ml[i].items.pop(0)
            ml[i].cnt_in += 1
            arg = w
            if not ml[i].oparg == 'old':
                arg = int(ml[i].oparg)
            if ml[i].op == '+':
                w = w + arg
            if ml[i].op == '*':
                w = w * arg
            w = int(w // 3)
            if w % ml[i].tst == 0:
                ml[ml[i].tst_true].items.append(w)
            else:
                ml[ml[i].tst_false].items.append(w)

for m in ml:
    print(m)

a = sorted([m.cnt_in for m in ml], reverse=True)
print(a[0]*a[1])
