# Create a function that returns the sum of the two lowest positive numbers
# given an array of minimum 4 positive integers. No floats or non-positive
# integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77],
# the output should be 7.

def sum_two_smallest_numbers(numbers):
    smallest = min(numbers)
    numbers.remove(smallest)
    secondSmallest = min(numbers)
    return smallest + secondSmallest

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13)
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]) == 19)
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]) == 30)
