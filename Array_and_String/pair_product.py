# input - list of numbers, target_product
# output - a tuple containing the indices that produce the product
# create an empty object to store the quotient of the target and the num
# iterate thru the list of nums
# get the quotient of the target_product and the num
# if the dictionary contains the num, return a tuple containing 
#    the dictionarys key value for the num and the current index.
# if not, add the quotient of the target_product and the num to the 
#    dictionary with its value the value of i 

def pair_product(nums, target_product, i = 0, quotients = {}):
    if nums[i] in quotients: return (quotients[nums[i]], i)

    complement = target_product / nums[i]
    quotients[complement] = i

    return pair_product(nums, target_product, i + 1, quotients)

print(pair_product([3, 2, 5, 4, 1], 8))