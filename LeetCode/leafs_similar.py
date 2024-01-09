from typing import Optional
from binary_tree_helper import TreeNode, to_binary_tree


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = self.get_leafs(root1)
        print('leafs1', leafs1)
        leafs2 = self.get_leafs(root2)
        print('leafs2', leafs2)
        return leafs1 == leafs2

    def get_leafs(self,root):
        if root == None:
            return []

        if root.left == None and root.right == None:
            return [root.val] 

        left = self.get_leafs(root.left)
        right = self.get_leafs(root.right)

        return left + right
    


root1 = [1,2]
root2 = [2,2]

root1 = to_binary_tree(root1)
root2 = to_binary_tree(root2)

sol = Solution()
sol.leafSimilar(root1,root2)

