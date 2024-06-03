def anagrams(s1, s2):
    return frequency(s1) == frequency(s2)

def frequency(s):
    output = {}
    for char in s:
        output[char] = output.get(char, 0) + 1
    return output

print(anagrams('monkeyswrite', 'newyorktimes'))
#print(anagrams('cats', 'tocs'))