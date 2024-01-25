"""
1457. Pseudo-Palindromic Paths in a Binary Tree
"""

from binary_tree_helper import TreeNode, to_binary_tree
from typing import Optional


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        path = set()
        
        return self.isPalindrom(root, path)

        


    def isPalindrom(self, node, path):
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

        
        return self.isPalindrom(node.left,path) + self.isPalindrom(node.right,path)

root = to_binary_tree([8,8,None,7,7,None,None,2,4,None,8,None,7,None,1])

s = Solution()

print(s.pseudoPalindromicPaths(root))