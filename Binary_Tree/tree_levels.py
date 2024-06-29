class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f



def tree_levels(root, levels = {}, level = 0):
    if root is None: return []

    levels.setdefault(level, []).append(root.val)
    tree_levels(root.left, levels, level + 1)
    tree_levels(root.right, levels, level + 1)

    return list(levels.values()) 

print(tree_levels(a)) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]