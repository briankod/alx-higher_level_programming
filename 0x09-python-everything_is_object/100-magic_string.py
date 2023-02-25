#!/usr/bin/python3

# The magic_string function takes a single argument a, which defaults to
# an empty list if no value is provided when the function is called.
# The function then appends the string "BestSchool" to the list a using
# the += operator, which modifies the original list.
# Finally, the function returns a string containing all the elements of
# a, separated by commas and a space, using the join() method with ", "
# as the separator.
# It's worth noting that because the default argument value is mutable
# (a list), if magic_string is called multiple times without explicitly
# passing in a new list as an argument, the same list object will be
# used and appended to each time.
def magic_string(a=[]):
    a += ["BestSchool"]
    return (", ".join(a))

#  A function magic_string() that returns a string “BestSchool” n times
# the number of the iteration
