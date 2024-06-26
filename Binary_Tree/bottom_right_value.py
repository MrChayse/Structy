class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(3)
b = Node(11)
c = Node(10)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1
from collections import deque

def bottom_right_value(root):
    if not root: return None
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        output = curr.val
        queue.extend(val for val in (curr.left, curr.right) if val)
    
    return output
print(bottom_right_value(a)) # -> 1