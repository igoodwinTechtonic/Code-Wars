# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'

def solution(string):
    return string[::-1]

def tests():
    if solution('world') != 'dlrow':
        print('Not correct')
    if solution('hello') != 'olleh':
        print('Not Correct')

tests()
