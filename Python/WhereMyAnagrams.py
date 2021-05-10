# What is an anagram? Well, two words are anagrams of each other if they
# both contain the same letters. For example:

# 'abba' & 'baab' == true

# 'abba' & 'bbaa' == true

# 'abba' & 'abbba' == false

# 'abba' & 'abca' == false

# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words. You should
# return an array of all the anagrams or an empty array if there are none.

def letterCount(word):
    letterDict = {}
    for l in word:
        if letterDict.get(l) is None:
              letterDict[l] = word.count(l)
    return letterDict

def anagrams(word, words):
    anagramsList = []
    # Count characters and place in dict
    anagram = letterCount(word)

    for w in words:
        if letterCount(w) == anagram:
            anagramsList.append(w)
    return anagramsList

# def anagrams(word, words):
#   return [item for item in words if sorted(item)==sorted(word)]

# def anagrams(word, words):
#     return filter(lambda x: sorted(word) == sorted(x), words)

# from collections import Counter
# def anagrams(word, words):
#     counts = Counter(word)
#     return [w for w in words if Counter(w) == counts]

# def anagrams(word, words):
#     match = sorted(word)
#     return [w for w in words if match == sorted(w)]

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])) # == ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])) # == ['carer', 'racer'])
