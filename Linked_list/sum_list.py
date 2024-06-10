class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

def sum_list(head, output = 0):
    if head == None: return output

    output += head.val
    return sum_list(head.next, output)

print(sum_list(a))