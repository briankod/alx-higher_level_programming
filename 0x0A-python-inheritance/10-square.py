#!/usr/bin/python3
"""
A class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Module of a square"""
    def __init__(self, size):
        """Initializes the square attributes


        Args:
            size (int): Describes the length of a square


        Returns:
            None
        """
        # condition to check whether 'size' is suitable or not
        self.integer_validator("size", size)
        self.__size = size
        # The Rectangle class has an __init__() method that takes two
        # parameters width and height, while the Square subclass only
        # needs to specify one parameter size because a square has
        # equal width and height. Therefore, when the Square subclass
        # calls super().__init__(size, size), it initializes the width
        # and height attributes of the Rectangle class with the same
        # value size.
        super().__init__(size, size)

    def area(self):
        """Calculates area of a square


        Returns:
            the square area
        """
        return(self.__size ** 2)

# A class Square that inherits from Rectangle (9-rectangle.py):
# Instantiation with size: 'def __init__(self, size):':
# size must be private. No getter or setter
# size must be a positive integer, validated by integer_validator
# the area() method must be implemented
