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

def all_tree_paths(root, path = [], paths = []):
    if root is None: return paths
    path.append(root.val)
    if root.left is None and root.right is None: 
        paths.append(path.copy())    
  
    all_tree_paths(root.left, path, paths)
    all_tree_paths(root.right, path, paths)
    
    path.pop()

    return paths

print(all_tree_paths(a)) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ] 
