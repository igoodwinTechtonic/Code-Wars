# Square every digit of a number and concatenate them
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# MY SOLUTION

import math

def square_digits(num: int):
    digits = str(num)
    concatenated = ''
    for digit in digits:
        concatenated = concatenated + str(int(math.pow(int(digit), 2)))
    return int(concatenated)

print(square_digits(23), square_digits(23) == 49)
print(square_digits(111), square_digits(111) == 111)
print(square_digits(345), square_digits(345) == 91625)

# OTHER SOLUTIONS

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
