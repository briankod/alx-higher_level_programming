#!/usr/bin/python3
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

    def my_print(self):
        """Prints in stdout the square with the character #

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        # In this code, we use a list comprehension to create a list of n "#"
        # characters, and then use the join() method to concatenate them with
        # a space character between them. The print() statement at the end of
        # each row adds a newline character to start a new row.
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

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
# ...
# Public instance method: def my_print(self): that prints in
# stdout the square with the character #
# if size is equal to 0, print an empty line
