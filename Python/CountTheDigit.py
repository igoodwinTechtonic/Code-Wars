# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.
# Square all numbers k (0 <= k <= n) between 0 and n.
# Count the numbers of digits d used in the writing of all the k**2.
# Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.

def nb_dig(n, d):
    count = 0
    for x in range(0, n + 1):
        count += (str(x * x)).count(str(d))
    return count

print(nb_dig(5750, 0), 4700)
print(nb_dig(11011, 2), 9481)
print(nb_dig(12224, 8), 7733)
print(nb_dig(11549, 1), 11905)

# Other solutions

def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))

def nb_dig(n, d):
    return ''.join(str(a ** 2) for a in xrange(n + 1)).count(str(d))
