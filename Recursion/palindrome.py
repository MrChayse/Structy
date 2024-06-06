# input - string
# output - boolean if string is same reversed
# initialize i variable to 0 and j to None
# if j is None assign j the value of the len of the input string - 1.
# if index i is not equal to index j, return false.
# else return the function incrementing i decrementing j

def palindrome(s, i = 0, j = None):
    if j is None: j = len(s) - 1
    if i >= j: return True
    if s[i] != s[j]: return False
    else: return palindrome(s, i + 1, j - 1)

print(palindrome("rotator"))