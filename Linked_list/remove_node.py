
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f 

# input - head of a linked list, and a target value
# output - return the head of the resulting linked list with the 
    # node containing the target value deleted.
# traverse thru the linked list
# if the nodes value is equal to the taret value:
    # link the previous node to the next node.
# return the head.next.

def remove_node(head, target, prev = None):
    if prev == None and head.val == target: return head.next
    
    if head.val == target:
       prev.next = head.next
       return prev.next
    head.next = return remove_node(head.next, target, head)
    return head


print(remove_node(a, "c"))
# a -> b -> d -> e -> f