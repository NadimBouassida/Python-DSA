"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

"""


# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# creating Nodes manually
# [2,null,3,null,4,null,5,null,6]
a = Node(2)
c = Node(3)
e = Node(4)
g = Node(5)
i = Node(6)

# creating Links manually
a.right = c
c.right = e
e.right = g
g.right = i

class Solution:
    def minDepth(self, root: Node, depth = 1) -> int:
        if root is None:
            return 0
        
        queue = [root]
        depth = 1
        while len(queue) != 0:
            size = len(queue)
            while size > 0:
                size -= 1
                node = queue.pop(0) 
                if node == None:
                    continue

                if node.left == None and node.right == None:
                    return depth

                queue.append(node.left)
                queue.append(node.right)
            depth += 1
        return -1


sol = Solution()

print(sol.minDepth(a))
print(sol.minDepth(Node()))
        