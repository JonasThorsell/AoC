import sys
import itertools

s1,s2 = 0,0
for l in sys.stdin:
    a,b = l.split(':')
    tst = int(a)
    nums = list(map(int, b.split()))
    for ops in itertools.product('+*', repeat=len(nums)-1):
        s = nums[0]
        for n,o in zip(nums[1:],ops):
            if o == '+':
                s += n
            else:
                s *= n
        if s == tst:
            s1 += s
            break
    for ops in itertools.product('+*|', repeat=len(nums)-1):
        s = nums[0]
        for n,o in zip(nums[1:],ops):
            if o == '+':
                s += n
            elif o == '*':
                s *= n
            else:
                s = int(str(s)+str(n))
        if s == tst:
            s2 += s
            break

print(s1)
print(s2)


