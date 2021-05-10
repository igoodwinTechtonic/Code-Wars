# Is a number prime?

# Define a function that takes one integer argument and returns logical
# value true or false depending on if the integer is a prime

# You can assume you will be given an integer input.

# You can not assume that the integer will be only positive. You may be
# given negative numbers as well (or 0).

# NOTE on performance: There are no fancy optimizations required, but
# still the most trivial solutions might time out. Numbers go up to
# 2^31 or 2,147,483,648 (or similar, depends on language version). Looping all the way
# up to n, or n/2, will be too slow.

import pytest

def is_prime(num):
    # Return false for negatives and even numbers, except 2
    if num <= 1: return False
    if num == 2 or num == 3 or num == 5: return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False

    i = 5
    while i ** 2 < num:
        if num % i == 0 or num % (i + 2) == 0: return False
        i += 6

    return True

numbers = [
    (5, True),
    (9, False),
    (17, True),
    (25, False),
    (30, False),
    (37, True),
]

@pytest.mark.parametrize('num, result', numbers)
def test_prime(num, result):
    assert is_prime(num) == result
