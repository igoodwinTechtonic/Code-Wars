# Write a program that will calculate the
# number of trailing zeros in a factorial
# of a given number.

import re

def zeros(n):
    return len(re.search("0*$", str(n)).group())

print(zeros(23000000))
