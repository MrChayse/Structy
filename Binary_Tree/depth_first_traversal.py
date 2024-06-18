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

def depth_first_values(root, memo = {}):
  if not root:
    return []
  if root in memo: return memo[root]
  
  left_values = depth_first_values(root.left, memo)
  right_values = depth_first_values(root.right, memo)

  output = [root.val, *left_values, *right_values]
  memo[root] = output

  return output




depth_first_values(a)
#   -> ['a', 'b', 'd', 'e', 'c', 'f']