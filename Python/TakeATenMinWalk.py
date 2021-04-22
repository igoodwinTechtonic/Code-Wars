# You live in the city of Cartesia where all roads are laid out in a 
# perfect grid. You arrived ten minutes too early to an appointment, 
# so you decided to take the opportunity to go for a short walk. The 
# city provides its citizens with a Walk Generating App on their phones
# -- everytime you press the button it sends you an array of one-letter
# strings representing directions to walk (eg. ['n', 's', 'w', 'e']).
# You always walk only a single block for each letter (direction) and
# you know it takes you one minute to traverse one city block, so create
#  a function that will return true if the walk the app gives you will
# take you exactly ten minutes (you don't want to be early or late!) and
# will, of course, return you to your starting point. Return false otherwise.

# Note: you will always receive a valid array containing a random assortment
# of direction letters ('n', 's', 'e', or 'w' only). It will never give you
# an empty array (that's not a walk, that's standing still!).

def is_valid_walk(walk):
    if len(walk) != 10: return False
    if walk.count('n') != walk.count('s'): return False
    if walk.count('e') != walk.count('w'): return False
    return True

# def isValidWalk(walk):
#     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # True
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])) # False
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])) # False
print(is_valid_walk(['w'])) # False
print(is_valid_walk(['e', 'n', 'e', 'w', 'w', 's', 'w', 'e'])) # True
print(is_valid_walk(['e', 's', 'e', 'n', 'w', 'n', 'w', 's'])) # True
