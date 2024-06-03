from collections import Counter

def anagrams(s1, s2):
    if len(s1) != len(s2): return False

    frequency = dict(Counter(list(s1)))
    letters = list(s2)

    for letter in letters:
        if letter in frequency: frequency[letter] -= 1 
    return all([val == 0 for val in frequency.values()])

#print(anagrams('restful', 'fluster'))
print(anagrams('catss', 'tocs'))
#print(anagrams('monkeyswrite', 'newyorktimes'))    
                     