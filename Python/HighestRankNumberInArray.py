# Complete the method which returns the number which is most frequent in the given input array.
# If there is a tie for most frequent number, return the largest number among them.

# Note: no empty arrays will be given.

def highest_rank(arr: list):
    maxcount = (0, 0)
    for num in arr:
        count = arr.count(num)
        if (count > maxcount[1]):
            maxcount = (num, count)
        if (count == maxcount[1]):
            maxcount = (num if num > maxcount[0] else maxcount[0], count)
    return maxcount[0]

print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]), 12)
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)

# Other solutions

from collections import Counter
def highest_rank(arr: list):
    if arr:
        c = Counter(arr)
        m = max(c.values())
        return max(k for k, v in c.items() if v == m)

from collections import Counter
def highest_rank(arr):
    return max(Counter(arr).items(), key = lambda x: [x[1], x[0]])[0]

from collections import Counter
def highest_rank(arr):
    c = Counter(arr)
    return max(c, key=lambda x: (c[x], x))

def highest_rank(arr: list):
    return sorted(arr, key = lambda x: (arr.count(x), x))[-1]

def highest_rank(arr):
    return max(sorted(arr, reverse = True), key = arr.count)
