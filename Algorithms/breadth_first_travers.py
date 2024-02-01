"""
    Implementing breadth-first traversal iteratively with a queue data structure offers several advantages over a recursive approach using stacks.
    By processing nodes level by level, the iterative approach ensures efficient exploration of each level before moving on to the next,
    naturally fitting the FIFO (First-In-First-Out) structure of a queue. In contrast,
    implementing breadth-first traversal recursively involves simulating a queue using the call stack, 
    which can introduce additional complexity and overhead.
    Therefore, the iterative approach with a queue is generally preferred for its efficiency and simplicity.
"""
from DataStructures.binary_tree import to_binary_tree
from typing import Optional
from collections import deque

def breadth_first_travers(root):
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

root = to_binary_tree(['a','b','c','d','e','f'])
print(breadth_first_travers(root))



