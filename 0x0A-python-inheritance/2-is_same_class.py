#!/usr/bin/python3
"""
A function that checks if object is exactly
an instance of the specified class.
"""


# type() function returns the type of an object, and it returns a class object
# representing the type. For example, type(10) returns <class 'int'>,
# indicating that 10 is an integer. type() can be used to check the
# exact type of an object, and it's commonly used in conditional
# statements to check if an object is of a specific type.
def is_same_class(obj, a_class):
    """Returns True if condition passes ; otherwise False."""
    return(type(obj) == a_class)

# A function that returns True if the object is exactly an instance of the
# specified class ; otherwise False.
