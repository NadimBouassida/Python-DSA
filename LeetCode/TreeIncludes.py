# Implementation of a node calss
class Node():
    def __init__(self, val = None) -> None:
        self.val = val
        self.left = None
        self.right = None

# Some nodes examples to work with
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

# Manually creating the binary tree
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def treeIncludes(root, target):
    if root == None:
        return False
    queue = [root]

    while (len(queue) > 0):
        current = queue.pop(0)
        if current.val == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False

print(treeIncludes(a,'e'))
print(treeIncludes(a,'j'))
    