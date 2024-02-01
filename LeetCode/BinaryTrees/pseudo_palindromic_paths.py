"""
1457. Pseudo-Palindromic Paths in a Binary Tree
"""

from DataStructures.binary_tree import TreeNode, to_binary_tree
from typing import Optional


class Solution:
    def pseudo_palindromic_paths (self, root: Optional[TreeNode]) -> int:

        path = set()
        
        return self.is_palindrom(root, path)

        


    def is_palindrom(self, node, path):
        if not node:
            return 0

        if not node.left and not node.right:
            if len(path) <= 1:
                return 1
            else:
                return 0

        if node.val in path:
            path.remove(node.val)
        else:
            path.add(node.val)

        
        return self.is_palindrom(node.left,path) + self.is_palindrom(node.right,path)

root = to_binary_tree([8,8,None,7,7,None,None,2,4,None,8,None,7,None,1])

s = Solution()

print(s.pseudo_palindromic_paths(root))