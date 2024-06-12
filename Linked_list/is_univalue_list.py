# input - head of a linked list
# output - Boolean indicating whether or not the linked list contains
    # exactly one unique value
# traverse thru the linked list
# if the nodes next property is None return if the val_list has a length of 1
# initialize a val_list variable to an empty list.
# if the current nodes value is not in the val_list, append the it with 
    # the current nodes value.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
a = Node(7)
b = Node(7)
c = Node(7)

a.next = b
b.next = c

def is_univalue_list(head, prev_val = None):
    if head is None: return True
    if prev_val is None or head.val == prev_val:
        return is_univalue_list(head.next, head.val)
    else:
        return False

print(is_univalue_list(a))