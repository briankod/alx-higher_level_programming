#!/usr/bin/python3

# "def area(self): ” , here "self" is used as a parameter in the method
# because whenever we call the method, the object (instance of class)
# is automatically passed as a first argument along with other
# arguments of the method.
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

    def area(self):
        """Calculates area of a square


        Returns:
            the current square area
        """
        return (f"{self.__size*self.__size}")

# Private instance attribute: size
# Instantiation with optional size: def __init__(self, size=0):
# ...
# Public instance method: def area(self): that returns the current square area
