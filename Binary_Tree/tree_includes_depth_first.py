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

def tree_includes(root, target):
    if root is None: return False
    if root.val is target: return True
    return tree_includes(root.left, target) or tree_includes(root.right, target)