from DataStructures.binary_tree import TreeNode, to_binary_tree
from typing import Optional
#Iterative approach:
def depth_first_travers_iter(root:Optional[TreeNode]):
    res = []
    stack = [root]
    while len(stack) != 0:
        current = stack.pop()
        res.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return res


# Recurrsive approach:
def depth_first_travers_recur(root):
    if root == None:
        return []
    
    leftValues = depth_first_travers_recur(root.left)
    rightValues = depth_first_travers_recur(root.right)

    return [root.val] + leftValues + rightValues


root = to_binary_tree(['a','b','c','d','e','f'])

print(depth_first_travers_iter(root))
print(depth_first_travers_recur(root))