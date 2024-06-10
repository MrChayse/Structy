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

def linked_list_values(head, output = []):
    if head == None: return output

    output.append(head.val)
    return linked_list_values(head.next, output)

print(linked_list_values(a))