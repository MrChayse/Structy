class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

def leaf_list(root, output = []):
    if root is None: return output
    if root.left is None and root.right is None: output.append(root.val)

    leaf_list(root.left, output)
    leaf_list(root.right, output)

    return output

print(leaf_list(a)) # -> [ 'd', 'e', 'f' ] 