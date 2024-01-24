"""
1026. Maximum Difference Between Node and Ancestor
"""
from binary_tree_helper import TreeNode, to_binary_tree
from typing import Optional


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        l_set = set()
        r_set = set()
        stack = [root]
        while stack:
            node = stack.pop()

            if node.right:
                stack.append(node.right)
                diff = node.val - node.right.val
                if r_set:
                    for val in r_set.copy():
                        r_set.add(val+diff)
                r_set.add(diff)

            if node.left:
                stack.append(node.left)
                diff = node.val - node.left.val
                if l_set:
                    for val in l_set.copy():
                        l_set.add(val+diff)
                l_set.add(diff)
        
        l_set.update(r_set)
        v_set = l_set
        map_v_set = map(abs,v_set)
        return max(map_v_set)


root = to_binary_tree([8,3,10,1,6,None,14,None,None,4,7,13])

sol = Solution()
print(sol.maxAncestorDiff(root))