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

def breadth_first_values(root):
    if not root: return []
    queue = [root]
    output = []
    while queue:
        curr = queue.pop()
        output.append(curr.val)
        queue = [val for val in(curr.right, curr.left) if val] + queue
    
    return output

print(breadth_first_values(a))