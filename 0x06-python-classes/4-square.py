#!/usr/bin/python3

# Getters: These are the methods used in Object-Oriented Programming (OOPS)
# which helps to access the private attributes from a class.
# Setters: These are the methods used in OOPS feature which helps to set
# the value to private attributes in a class.
# @property is used to get the value of a private attribute without using
# any getter methods. We have to put a line @property in front of the
# method where we return the private variable.
# To set the value of the private variable, we use @method_name.setter in front
# of the method. We have to use it as a setter.
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
        self.size = size

    def area(self):
        """Calculates area of a square


        Returns:
            the current square area
        """
        return (f"{self.__size*self.__size}")

    @property
    def size(self):
        """getting the size


        Returns:
            the length of a square
        """
        return(self.__size)

    @size.setter
    def size(self, value):
        """setting the size


        Args:
            value (int): Describes the length of a square


        Returns:
            None
        """
        # condition to check whether 'value' is suitable or not
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

# Private instance attribute: size
# property def size(self): to retrieve it
# property setter def size(self, value): to set it
# ...
