# input - 2 lists a, b
# output - a list containing the elements that are in both lists NO duplicates.
# data structures - lists, set
# create a set out of the list a to remove all duplicates.
# create an empty output list
# iterate thru the list b
    # if the num is in the set append it to the output list.
# return the output list

def intersection(a, b):
    arr_a = set(a)
    output = [num for num in b if num in arr_a]
    return list(set(output))

print(intersection([4,2,1], [1,2,4,6]))