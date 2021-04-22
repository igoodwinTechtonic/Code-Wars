# You are going to be given a word. Your job is to return the middle character
# of the word. If the word's length is odd, return the middle character. If
# the word's length is even, return the middle 2 characters.

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"

def get_middle(s):
    length = len(s)
    # if length == 1 or length == 2: return s
    # If even return two middle characters
    if length % 2 == 0:
        return s[length // 2 - 1] + s[length // 2]
    return s[length // 2]

# def get_middle(s):
#    return s[(len(s)-1)/2:len(s)/2+1]

# def get_middle(s):
#     i = (len(s) - 1) // 2
#     return s[i:-i] or s

print(get_middle("test") == "es")
print(get_middle("testing") == "t")
print(get_middle("middle") == "dd")
print(get_middle("A") == "A")
print(get_middle("of") == "of")