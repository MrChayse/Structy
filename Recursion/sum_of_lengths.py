# input - list of strings
# output - total length of the strings
# create an output variable initialized to 0
# access each string in the list and add its's length value to output
# once the last string is added to output, return output.

def sum_of_lengths(strings, i = 0, output = 0):
    if i == len(strings): return output

    output += len(strings[i])
    return sum_of_lengths(strings, i + 1, output)

print(sum_of_lengths(['bike', 'at', 'pencils', 'phone']))