# input - number representing the nth number of the fibonacci sequence.
# output - the value of the input number represents in the fibonacci sequence.
# initialize a cache object as an empty dictionary
# if the number is equal to 0 return 0
# if the number is less than or equal to 2, return 1
# if the input number is in cache, return its value.
# if not, assign the value of the number in cache to its fib value.

def fibonacci(n, cache = {}):
    if n == 0: return 0
    if n <= 2: return 1
    if n in cache: return cache[n]
    else:
        cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
        return cache[n]
print(fibonacci(6))