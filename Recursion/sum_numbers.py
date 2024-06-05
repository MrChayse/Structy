def sum_numbers_recursive(nums, i = 0, sum = 0):
    if i == len(nums): return sum

    sum += nums[i]
    return sum_numbers_recursive(nums, i + 1, sum)

print(sum_numbers_recursive([123456789, 12345678, 1234567, 123456, 12345, 1234, 123, 12, 1, 0]))