# input: list of numbers and a target sum
# output: the indices of the numbers in the list that produce the target sum.
# create an empty dictionary to store the difference of the target sum
    # and the num with its value the number.
# on each iteration, check if the diff exists in the dictionary.
#   if not, add it to the dictionary with its value the num
#   if so return a tuple containing the key and value.

def pair_sum(nums, target_sum):
    differences = {}

    for i in range(len(nums)):
        diff = target_sum - nums[i]
        if nums[i] in differences:
            return (differences[nums[i]], i)
        else:
            differences[diff] = i

print(pair_sum([3, 2, 5, 4, 1], 8))