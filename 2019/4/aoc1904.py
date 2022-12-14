
def check1(n):
    if n[5]<n[4] or n[4]<n[3] or n[3]<n[2] or n[2]<n[1] or n[1]<n[0]:
        return False
    if n[0]==n[1] or n[1]==n[2] or n[2]==n[3] or n[3]==n[4] or n[4]==n[5]:
        return True
    return False

def check2(n):
    if n[5]<n[4] or n[4]<n[3] or n[3]<n[2] or n[2]<n[1] or n[1]<n[0]:
        return False
    if  (                   n[0]==n[1] and not n[1]==n[2]) or \
        (not n[0]==n[1] and n[1]==n[2] and not n[2]==n[3]) or \
        (not n[1]==n[2] and n[2]==n[3] and not n[3]==n[4]) or \
        (not n[2]==n[3] and n[3]==n[4] and not n[4]==n[5]) or \
        (not n[3]==n[4] and n[4]==n[5]                   ):
        return True
    return False

def inc(n):
    o = True
    for i in range(5,-1,-1):
        if int(n[i])+1>9:
            n[i]='0'
        else:
            n[i]=str(int(n[i])+1)
            return n
    return []

r0,r1 = input().strip().split('-')
r0,r1 = list(r0),list(r1)
n = r0.copy()
s1,s2=0,0
while int(''.join(n)) <= int(''.join(r1)):
    if check1(n):
        s1+=1
    if check2(n):
        s2+=1
    n = inc(n)

print(s1)
print(s2) # 1865 to low