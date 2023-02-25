#!/usr/bin/python3

# The type() function either returns the type of the object or
# returns a new type object based on the arguments passed.
# Syntax:
# type with single parameter:
# type(object)
# type with 3 parameters:
# type(name, bases, dict)
"""A class Square that defines a square"""


class Square:
    """Module of a square


    Attributes:
        __size (int): Describes the length of a square
    """
    def __init__(self, size=0):
        """Initializes the square attributes


        Args:
            size (int): Describes the length of a square


        Returns:
            None
        """
        # condition to check whether 'size' is suitable or not
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

# Private instance attribute: size
# Instantiation with optional size: def __init__(self, size=0):
# ...
