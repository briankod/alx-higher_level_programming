#!/usr/bin/python3
"""
A function that checks if object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


# issubclass() is used to check whether a class is a subclass of another
# class or not.
# Syntax:
# issubclass(subclass, superclass)
# Here, subclass is the class that you want to check whether it is a subclass
# of superclass or not. The function returns True if the subclass is a
# subclass of superclass, otherwise it returns False.
def inherits_from(obj, a_class):
    """Returns True if condition passes ; otherwise False."""
    # the function returns True only if obj is an instance of a subclass of
    # a_class (i.e., the type of obj is not equal to a_class and is a
    # subclass of a_class), and False otherwise.
    return(type(obj) != a_class and issubclass(type(obj), a_class))

# A function that returns True if the object is an instance of a class that
# inherited (directly or indirectly) from the specified class ; otherwise
# False.
