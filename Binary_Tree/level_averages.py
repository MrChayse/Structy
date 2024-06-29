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

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1


def level_averages(root, level = 1, levels = {}):
    if root is None: return []

    levels.setdefault(level, [0, 0])
    levels[level][0] += root.val
    levels[level][1] += 1
        
    level_averages(root.left, level + 1, levels)
    level_averages(root.right, level + 1, levels)

    return [total / count for total, count in levels.values()]    

    
print(level_averages(a)) # -> [ 3, 7.5, 1 ] 