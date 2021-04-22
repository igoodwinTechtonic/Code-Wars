# We need a function that can transform a number into a string.
# What ways of achieving this do you know?

def number_to_string(num):
    # Return a string of the number here!
    return str(num)

# def number_to_string(num):
#     return "{}".format(num)

print(number_to_string(67) == '67')
print(number_to_string(79585) == '79585')
print(number_to_string(79585) == "79585")
print(number_to_string(1+2) == '3')
print(number_to_string(1-2) == '-1')
