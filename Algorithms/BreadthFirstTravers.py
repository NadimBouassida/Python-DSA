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

# Iterative approach
"""
    The only way to implement a breadth First
    Traversal algorithm is the Iterative approach, by nature
    breadth first travers depends on queue data structure
    to be implemented correctly wich go against the nature
    of recurssive functions wich is built on stacks
"""
from collections import deque

def breadthFirstTraversIterative(root):
    if root == None:
        return []
    deq = deque([root])
    values = []
    while (len(deq) > 0):
        current = deq.popleft()
        values.append(current.val)
        if current.left:
            deq.append(current.left)
        if current.right:
            deq.append(current.right)
    return values

print(breadthFirstTraversIterative(a))



