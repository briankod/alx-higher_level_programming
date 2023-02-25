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
        self.__size = size

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
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

    # Comparison magic methods are special methods in Python that are used
    # to compare two objects. When you define these methods in your classes,
    # you can customize the behavior of comparison operators for objects of
    # that class.

    # lt(self, other): This method is used to check if one object is less
    # than another. It is called when the < operator is used.
    def __lt__(self, other):
        """Compare if square is less than another using area
        Args:
            other (Square): square used for comparison
        Returns:
            True or False
        """
        return self.size < other.size

    # le(self, other): This method is used to check if one object is less than
    # or equal to another. It is called when the <= operator is used.
    def __le__(self, other):
        """Compare if square is less than or equal to another using area
        Args:
            other (Square): square used for comparison
        Returns:
            True or False
        """
        return self.size <= other.size

    # eq(self, other): This method is used to check if two objects are equal.
    # It is called when the == operator is used.
    def __eq__(self, other):
        """Compare if square is equal to another using area
        Args:
            other (Square): square used for comparison
        Returns:
            True or False
        """
        return self.size == other.size

    # ne(self, other): This method is used to check if two objects are not
    # equal. It is called when the != operator is used.
    def __ne__(self, other):
        """Compare if square is not equal to another using area
        Args:
            other (Square): square used for comparison
        Returns:
            True or False
        """
        return self.size != other.size

    # ge(self, other): This method is used to check if one object is greater
    # than or equal to another. It is called when the >= operator is used.
    def __ge__(self, other):
        """Compare if square is greater than or equal to another using area
        Args:
            other (Square): square used for comparison
        Returns:
            True or False
        """
        return self.size >= other.size

    # gt(self, other): This method is used to check if one object is greater
    # than another. It is called when the > operator is used.
    def __gt__(self, other):
        """Compare if square is greater than another using area
        Args:
            other (Square): square used for comparison
        Returns:
            True or False
        """
        return self.size > other.size

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
        if type(value) is not int or type(value) is not float:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

# Private instance attribute: size
# ...
# Instantiation with size: def __init__(self, size=0):
# ...
# Square instance can answer to comparators: ==, !=, >, >=, < and <= based
# on the square area
