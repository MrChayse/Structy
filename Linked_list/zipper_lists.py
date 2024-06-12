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
# Create a counter variable
# If count is even point to head_2, else point ot head_1
# if head_1 is exhausted, add the rest of head_2
# if head_2 is exhausted, add the rest of head_1
def zipper_lists(head_1, head_2):
    tail = head_1
    curr1 = head_1.next
    curr2 = head_2
    count = 0

    while curr1 is not None and curr2 is not None:
        if count % 2 == 0:
            tail.next = curr2
            curr2 = curr2.next
        else:
            tail.next = curr1
            curr1 = curr1.next
        tail = tail.next
        count += 1

        if curr1 is not None:
            tail.next = curr1
        if curr2 is not None:
            tail.next = curr2

    return head_1

print(zipper_lists(a, x))