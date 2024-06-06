# input - number
# the factorial of the input number
    # factorial of 6 example: 6 * 5 * 4 * 3 * 2 * 1 = 720
# create an output variable to the value of 1
# multiply the output by each the input number
# decrement the input number by 1
# if the input number is 1 return output

def factorial(num, output = 1):
    if num <= 1: return output

    output *= num
    return factorial(num -1, output)

print(factorial(18))