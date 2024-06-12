# input - 2 sorted linked lists
# output - 1 sorted linked list from the 2 input lists merged together.
# if either node is None return the other list or None if both are None 
# determine the current node by which has the least value.
# traverse to the next node from the list that the node was accessed.
# return the merged list

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(1)
r = Node(8)
s = Node(9)
t = Node(10)

q.next = r
r.next = s
s.next = t
# 1 -> 8 -> 9 -> 10

def merge_lists(h1, h2):
    if not h1 or not h2: return h1 or h2
    
    if h1.val < h2.val:
        h1.next = merge_lists(h1.next, h2)
        return h1
    else:
        h2.next = merge_lists(h1, h2.next)
        return h2
       
       


