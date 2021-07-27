# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
#   plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand,
#   the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:

def zero(n = 0):
  if isinstance(n, str): return logic(str(0) + ' ' + n)
  return n
def one(n = 1):
  if isinstance(n, str): return logic(str(1) + ' ' + n)
  return n
def two(n = 2):
  if isinstance(n, str): return logic(str(2) + ' ' + n)
  return n
def three(n = 3):
  if isinstance(n, str): return logic(str(3) + ' ' + n)
  return n
def four(n = 4):
  if isinstance(n, str): return logic(str(4) + ' ' + n)
  return n
def five(n = 5):
  if isinstance(n, str): return logic(str(5) + ' ' + n)
  return n
def six(n = 6):
  if isinstance(n, str): return logic(str(6) + ' ' + n)
  return n
def seven(n = 7):
  if isinstance(n, str): return logic(str(7) + ' ' + n)
  return n
def eight(n = 8):
  if isinstance(n, str): return logic(str(8) + ' ' + n)
  return n
def nine(n = 9):
  if isinstance(n, str): return logic(str(9) + ' ' + n)
  return n

def plus(n = 0):
    return '+ %d' % n
def minus(n = 0):
    return '- %d' % n
def times(n = 1):
    return '* %d' % n
def divided_by(n = 1):
    return '/ %d' % n

def logic(statement: str):
    chars = statement.split(' ')
    operand = chars[1]
    num1 = int(chars[0])
    num2 = int(chars[2])
    if (operand == '+'): return num1 + num2
    if (operand == '-'): return num1 - num2
    if (operand == '*'): return num1 * num2
    if (operand == '/'): return int(num1 / num2)
    return 0

print(seven(times(five())), 35)
print(four(plus(nine())), 13)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)


# Other solutions

def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda x: x*y
def divided_by(y): return lambda x: x/y


id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x
