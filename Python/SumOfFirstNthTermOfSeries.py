# Your task is to write a function which returns the
# sum of following series up to nth term(parameter).

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + ...

# You need to round the answer to 2 decimal places and return it as String.
# If the given value is 0 then it should return 0.00
# You will only be given Natural Numbers as arguments.

def series_sum(n: int):
    if (n == 1): return "1.00"
    return str("%.2f" % round(doTheMath(n), 2))

def doTheMath(n: int):
    if (n == 0): return 0
    return doTheMath(n - 1) + (1 / (1 + 3 * (n-1)))

print(series_sum(1), "1.00")
print(series_sum(2), "1.25")
print(series_sum(3), "1.39")
print(series_sum(5), "1.57")


# Other solutions

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

def series_sum(n):
    sum = 0.0
    for i in range(0, n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum

