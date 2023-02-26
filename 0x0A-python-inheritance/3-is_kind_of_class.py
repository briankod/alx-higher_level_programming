#!/usr/bin/python3
"""
A function that checks if object is an instance of, or if
object is an instance of a class that inherited from,
the specified class.
"""


# isinstance() function checks whether an object is an instance of a specified
# class or any of its subclasses. It returns True if the object is an instance
# of the class or a subclass of it, and False otherwise. For example,
# isinstance(10, int) returns True because 10 is an instance of the int class.
# isinstance() can be used to check if an object is of a specific class or a
# subclass of it.
# In summary,the main difference between type() and isinstance() is that type()
# returns the exact type of an object, whereas isinstance() checks if an object
# is an instance of a specified class or its subclasses. Depending on the use
# case, one function may be more appropriate than the other.
def is_kind_of_class(obj, a_class):
    """Returns True if condition passes ; otherwise False."""
    return(isinstance(obj, a_class))

# A function that returns True if the object is an instance of, or if
# the object is an instance of a class that inherited from, the
# specified class ; otherwise False.
