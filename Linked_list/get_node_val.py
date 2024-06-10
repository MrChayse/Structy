class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

def get_node_value(head, index, count = 0):
    if head is None: return None
    if index == count: return head.val

    return get_node_value(head.next, index, count + 1)

print(get_node_value(a, 2))