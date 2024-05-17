"""
1325. Delete Leaves With a Given Value
"""
from typing import Optional
from bin_tree_helper import TreeNode, listToBinTree

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode],target: int) -> Optional[TreeNode]:
        if not root:
            return

        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right,target)

        if not root.left and not root.right:
            if root.val == target:
                root = None
                return 


        return root
    

# test pass successfuly in leetcode