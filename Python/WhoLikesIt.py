# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items. We want to
# create the text that should be displayed next to such an item.

# Implement a function likes :: [String] -> String, which must take
# in input array, containing the names of people who like an item.
# It must return the display text as shown in the examples:

# likes([]) # must be "no one likes this"
# likes(["Peter"]) # must be "Peter likes this"
# likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
# likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
# likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

def likes(names):
    length = len(names)

    if length == 0:
        return 'no one likes this'
    elif length == 1:
        return str(names[0]) + ' likes this'
    elif length == 2:
        return str(names[0]) + ' and ' + str(names[1]) + ' like this'
    elif length == 3:
        return str(names[0]) + ', ' + str(names[1]) + ' and ' + str(names[2]) + ' like this'
    else :
        people = names[:2]
        return str(people[0]) + ', ' + str(people[1]) + ' and ' + str(length - 2) + ' others like this'

# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this', 
#         2: '{} and {} like this', 
#         3: '{}, {} and {} like this', 
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)

# def likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return "%s likes this" % names[0]
#     elif len(names) == 2:
#         return "%s and %s like this" % (names[0], names[1])
#     elif len(names) == 3:
#         return "%s, %s and %s like this" % (names[0], names[1], names[2])
#     else:
#         return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)

"""
def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.
    
    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4
    
    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others = length - 2)
"""

print(likes([]) == 'no one likes this')
print(likes(['Peter']) == 'Peter likes this')
print(likes(['Jacob', 'Alex']) == 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this')
