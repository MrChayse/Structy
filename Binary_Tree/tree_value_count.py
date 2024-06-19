class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

def tree_value_count(root, target, count = 0):
    if root is None: return 0

    match = 1 if root.val == target else 0
    return match + tree_value_count(root.left, target, count) + tree_value_count(root.right, target, count)

    return match

print(tree_value_count(a,  6)) # -> 3