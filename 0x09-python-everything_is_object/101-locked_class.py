#!/usr/bin/python3
"""A class LockedClass with no class or object attribute"""


# The __slots__ attribute is used to define a fixed set of allowed instance
# attributes for the class. In this case, the only allowed instance attribute
# is first_name. Attempting to assign any other attribute to an instance of
# this class will raise an AttributeError.
# By using __slots__, you can save memory and improve performance for instances
# of this class, because Python does not need to create a dictionary to store
# instance attributes. Instead, it stores the attribute values in a tuple-like
# structure that is more memory-efficient.
class LockedClass:
    """The module prevents the user from dynamically creating new instance
    attributes,except if the new instance attribute is called first_name"""
    __slots__ = ["first_name"]

# A class LockedClass with no class or object attribute, that prevents the
# user from dynamically creating new instance attributes, except if the new
# instance attribute is called first_name.
