# Your function productFib takes an integer (prod) and returns an array:
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.

# If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prod you will return
# [F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(n) being the smallest one such as F(n) * F(n+1) > prod

def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]

# def productFib(prod):
#     func = lambda a, b: func(b, a+b) if a*b < prod else [a, b, a*b == prod]
#     return func(0, 1)

# My solution times out!

# def productFib(prod):
#     for x in range(1, 100):
#         n1 = Fibonacci(x)
#         n2 = Fibonacci(x+1)
#         if (prod < n1 * n2):
#             return [n1, n2, False]  
#         elif (prod == n1 * n2):
#             return [n1, n2, True]

# def Fibonacci(n):
#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")
 
#     # Check if n is 0
#     # then it will return 0
#     elif n == 0:
#         return 0
 
#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

print(productFib(15))
print(productFib(273))
