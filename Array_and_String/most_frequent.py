from functools import reduce

def most_frequent(s):
    arr = list(s)
    frequency = reduce(lambda acc, curr: {**acc, curr: acc.get(curr, 0) + 1}, arr, {})

    return max(frequency, key=frequency.get)

print(most_frequent('bookeeper'))