# input - list of numbers
# output - the list of numbers with all 5's appended to the end of the list
# data structures - list
# initialize i variable to 0, and j variable to the len property of the list.
# if the value at index i is 5 and the value at index j is not 5, swap them
# increment i, decrement j
# if i is equal to j, return the nums list

def five_sort(nums):
    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[j] == 5: j -= 1
        elif nums[i] == 5: nums[i], nums[j] = nums[j], nums[i]
        elif nums[i] != 5: i += 1
    return nums

print(five_sort([5, 5, 6, 5, 5, 5, 5]))