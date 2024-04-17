from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def listToBinTree(lst:List):
    def helper(node:Optional[TreeNode], idx, lst):
        l = len(lst) 
        left = 2*idx + 1
        right = 2*idx + 2
        if  left < l:
            node.left = TreeNode(lst[left])
            helper(node.left, left, lst)
        if right < l:
            node.right = TreeNode(lst[right])
            helper(node.right, right, lst)
        
        return node
    if not lst:
        return 
    
    root = TreeNode(lst[0])
    helper(root, 0 , lst)

    return root

def binTreeToList(root: Optional[TreeNode], stack = []):
    stack = []
    deq = deque([root])
    while deq:
        node = deq.popleft()
        stack.append(node.val)
        if node.left:
            deq.append(node.left)
        if node.right:
            deq.append(node.right)
    return stack
    