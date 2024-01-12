"""
1026. Maximum Difference Between Node and Ancestor
Solved
Medium
Topics
Companies
Hint
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3
 
"""

from typing import Optional
from binary_tree_helper import TreeNode, to_binary_tree

class Solution:
    def __init__(self):
        self.abs_max = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        curr_max = root.val
        curr_min = root.val

        self.get_max_diff(root.left,curr_max,curr_min)
        self.get_max_diff(root.right,curr_max,curr_min)

        

        return self.abs_max

    def get_max_diff(self, node, curr_max, curr_min):
        if not node:
            return 
        
        curr_max = max(curr_max, node.val)
        curr_min = min(curr_min, node.val)

        if node.left:
            self.get_max_diff(node.left,curr_max,curr_min)
        
        if node.right:
            self.get_max_diff(node.right,curr_max,curr_min)

        self.abs_max = max(self.abs_max,abs(curr_max - curr_min))


root = to_binary_tree([8,3,10,1,6,None,14,None,None,4,7,13])

sol = Solution()

print(sol.maxAncestorDiff(root))