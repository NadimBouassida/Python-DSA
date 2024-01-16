"""
1026. Maximum Difference Between Node and Ancestor
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
 

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105

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