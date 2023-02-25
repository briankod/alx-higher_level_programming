#!/usr/bin/python3

# The __init__ function is called every time an object is created from a class.
# The __init__ method lets the class initialize the object's attributes and
# serves no other purpose. It is only used within classes.
# In Python, the self keyword is used as a reference to the current instance
# of a class. When defining a class method, the first parameter is typically
# self, which refers to the object being operated on. By using self, you can
# access the object's attributes and methods within the class.
# Instance attributes: These are specific to an instance of a class and are
# created and accessed using the self keyword. Instance attributes are
# defined inside the class methods, usually in the __init__ method.
# They are used to store data that is unique to each instance.
# Access modifiers in Python are naming conventions that are commonly used to
# indicate the level of access that should be granted to a particular attribute
# or method. These naming conventions are as follows:
# 1. Public: Attributes and methods that are intended to be accessible
# from anywhere in the program can be named using regular
# names (i.e., no underscores).
# 2. Protected: Attributes and methods that are intended to be accessible
# only within the class and its subclasses can be named using a
# single underscore prefix.
# 3. Private: Attributes and methods that are intended to be accessible only
# within the class can be named using a double underscore prefix.
"""A class Square that defines a square"""


class Square:
    """Module of a square


    Attributes:
        __size (int): Describes the length of a square
    """
    def __init__(self, size):
        """Initializes the square attributes


        Args:
            size (int): Describes the length of a square


        Returns:
            None
        """
        self.__size = size

# Private instance attribute: size
# Instantiation with size (no type/value verification)
