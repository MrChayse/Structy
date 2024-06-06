# input - string
# output - The input stringin reverse order.
# initialize i and j variables to 0 None
# if j is equal to None, j is initialized to the len of the string
# if i is greater than or equal to j, return the string
# swap the values of index i and index j
# return the recursive call incrementing i, decrementing j, 

def reverse_string(s, i = 0, j = None):
    if j is None: 
        j = len(s) - 1
        s = list(s)
    if i >= j: return ''.join(s)

    s[i], s[j] = s[j], s[i]
    return reverse_string(s, i + 1, j - 1)

print(reverse_string("stopwatch"))    