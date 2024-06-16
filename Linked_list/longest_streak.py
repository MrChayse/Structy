# input - head of a linked list
# output - length of the longest consecutive streak of same values
    # within the list
# initialize a count variable to 1
# initialize a big_count variable to 0
# if the next nodes value is equal to the previous nodes value
    # increment count by 1
    # if count is greater than big count big_count equals count.
# else count is equal to 1
# if the node is None return teh value of big_count

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

def longest_streak(head, count = 1, big_count = 1):
    if head == None: return 0
    if head.next == None: return big_count

    if head.val == head.next.val:
       count += 1
       big_count = max(count, big_count)
    else:
       count = 1
    return longest_streak(head.next, count, big_count)

print(longest_streak(a))