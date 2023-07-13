# Implementation of a node calss
class Node():
    def __init__(self, val = None) -> None:
        self.val = val
        self.left = None
        self.right = None


# Manualy creating a nodes
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)
# Manualy implementing the links
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def treeSum(root):
    if root == None:
        return 0

    left_sum =  treeSum(root.left)
    right_sum = treeSum(root.right)

    return root.val + left_sum + right_sum

print(treeSum(a))



