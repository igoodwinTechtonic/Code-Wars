"""
Your goal in this kata is to implement a difference function, 
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in 
list b keeping their order.
"""

# My solution

def array_diff(a: list, b: list):
    if (len(a) == 0 | len(b) == 0): return a
    c: list = []
    for num in a:
        try: b.index(num)
        except ValueError: c.append(num)
    return c

# Best solution

def array_diff(a, b):
    return [x for x in a if x not in b]

def array_diff(a, b):
    #your code here
    return filter(lambda i: i not in b, a)

print(array_diff([1,2], [1]) == [2])
print(array_diff([1,2,2], [1]) == [2,2])
print(array_diff([1,2,2], [2]) == [1])
print(array_diff([1,2,2], []) == [1,2,2])
print(array_diff([], [1,2]) == [])
print(array_diff([1,2,3], [1,2]) == [3])
