class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z

# Base case - if both heads are None return None
# if head1 is None just return the rest of head2
# if head2 is None just return the rest of head1
# initialize next1 and next 2 variables for the next nodes in both lists
# assign head1 next to head2 to start the zipper
# head2 value is the recursive call on the next1 and next2 variables
# the return value is the head1 variable.
def zipper_lists(head_1, head_2):
    if not head_1 or not head_2:
        return head_1 or head_2
    
    head_1.next, head_2.next = head_2, zipper_lists(head_1.next, head_2.next)
    return head_1

print(zipper_lists(a, x))
    