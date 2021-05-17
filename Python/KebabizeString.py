# My solution

def kebabize(string: str):
    kList = []
    for char in string:
        if (char.isalpha() & (len(kList) == 0)):
            kList.append(char.lower())
        elif (char.isalpha() & (char.lower() != char)):
            kList.append(f'-{char.lower()}')
        elif (char.isalpha()):
            kList.append(char)
    return ''.join(kList)


# Other solutions

def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')

import re
def kebabize(s):
    return re.sub('\B([A-Z])', r'-\1', re.sub('\d', '', s)).lower()



print(kebabize('myCamelCasedString') == 'my-camel-cased-string')
print(kebabize('myCamelHas3Humps') == 'my-camel-has-humps')
print(kebabize('SOS') == 's-o-s')
print(kebabize('42') == '')
print(kebabize('CodeWars') == 'code-wars')

