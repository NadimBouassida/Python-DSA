# Implementation of a node calss
class Node():
    def __init__(self, val = None) -> None:
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return self.val

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

# def treeIncludesIterative(root, target):
#     if root == None:
#         return False
#     queue = [root]

#     while (len(queue) > 0):
#         current = queue.pop(0)
#         if current.val == target:
#             return True
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
#     return False

# print(treeIncludesIterative(a,'e'))
# print(treeIncludesIterative(a,'j'))

def treeIncludesRecurrsive(root, target):
    if root == None:
        return False
    
    if root.val == target:
        return True

    leftCheck = treeIncludesRecurrsive(root.left, target)
    rightCheck = treeIncludesRecurrsive(root.right, target)

    return leftCheck or rightCheck

print(treeIncludesRecurrsive(a,'e'))
print(treeIncludesRecurrsive(a,'j'))