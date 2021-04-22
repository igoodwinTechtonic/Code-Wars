# In this kata you will create a function that takes a list
# of non-negative integers and strings and returns a new 
# list with the strings filtered out.

def filter_list(l):
    filteredList = []
    for item in l:
        if not isinstance(item, str):
            filteredList.append(item)
    return filteredList

print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))

# def filter_list(l):
#     return [i for i in l if not isinstance(i, str)]

# def filter_list(l):
#     return [x for x in l if type(x) is not str]