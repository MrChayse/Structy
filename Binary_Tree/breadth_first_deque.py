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

from collections import deque

def breadth_first_values(root):
    if not root: return []
    queue = deque([root])
    output = []
    while queue:
        curr = queue.popleft()
        output.append(curr.val)
        queue.extend(val for val in (curr.left, curr.right) if val)
    
    return output

print(breadth_first_values(a))