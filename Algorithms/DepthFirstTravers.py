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


# Iterative approach:
# def depthFirstTraversIterative(root: Node):
#     stack = [root]
#     while len(stack) != 0:
#         current = stack.pop()
#         print(current.val)
#         if current.right:
#             stack.append(current.right)
#         if current.left:
#             stack.append(current.left)

# depthFirstTraversIterative(a)

# Recurrsive approach:
def depthFirstTraversRecurrsion(root):
    if root == None:
        return []
    
    leftValues = depthFirstTraversRecurrsion(root.left)
    rightValues = depthFirstTraversRecurrsion(root.right)

    return [root.val] + leftValues + rightValues

print(depthFirstTraversRecurrsion(a))