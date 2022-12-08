import sys
import anytree

def treesize(n):
    if hasattr(n, 'size'):
        return n.size
    s = 0
    for c in n.children:
        if not hasattr(c, 'size'):
            c.size = treesize(c)
        s += c.size
    n.size = s
    return s

root = anytree.Node('', type='dir')
wd = root

for l in sys.stdin:
    l = l.split()
    if l[0] == '$':
        if l[1] == 'cd':
            if l[2] == '/':
                wd = root
            elif l[2] == '..':
                wd = wd.parent
            else:
                for n in wd.children:
                    if n.type=='dir' and n.name==l[2]:
                        wd = n
    else:
        if l[0] == 'dir':
            n=anytree.Node(l[1], parent=wd, type='dir')
        else:
            n=anytree.Node(l[1], parent=wd, size=int(l[0]), type='file')

treesize(root)
print(sum([n.size for n in anytree.PreOrderIter(root) if n.type=='dir' and n.size<=100000]))
ns = 30000000 - (70000000 - root.size)
print(sorted([n.size for n in anytree.PreOrderIter(root) if n.type=='dir' and n.size>=ns])[0])
