# Implementation of a node calss
class Node():
    def __init__(self, val = None) -> None:
        self.val = val
        self.left = None
        self.right = None


# Manualy creating a nodes
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)
# Manualy implementing the links
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# Using the recurrsive approach

def minValueRecurrsive(root: Node):
    if root == None:
        return float('inf')

    if root.val == None:
        return 
    
    left_vals = minValueRecurrsive(root.left)
    right_vals = minValueRecurrsive(root.right)

    return min(root.val, left_vals, right_vals)

print(minValueRecurrsive(a))
print(minValueRecurrsive(Node()))


#Using the Iterative approach
from collections import deque

def minValueIterative(root: Node):
    if root == None:
        return

    deq = deque([root])
    min_val = root.val
    while len(deq) > 0:
        current = deq.popleft()
        if current.val:
            min_val = min(min_val, current.val)
        if current.left:
            deq.append(current.left)
        if current.right:
            deq.append(current.right)

    return min_val



print(minValueIterative(a))
print(minValueIterative(Node()))
