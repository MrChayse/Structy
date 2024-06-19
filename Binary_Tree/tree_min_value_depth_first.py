class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

import math

def tree_min_value(root):
    if root is None: return math.inf
    return  min(root.val, tree_min_value(root.left), tree_min_value(root.right))

print(tree_min_value(a))