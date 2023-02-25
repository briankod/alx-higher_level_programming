#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


# Class attributes: These are attributes that are shared among all instances of
# a class. They are defined outside of any method of the class and are accessed
# using the class name. Class attributes are also known as static variables.
class Rectangle:
    """Module of a rectangle


    Attributes:
        __width (int): Decribes the width of a rectangle
        __height (int): Describes the height of a rectangle
    """

    # number_of_instances is initialized to 0 as a class-level variable. In the
    # constructor (__init__), every time a new instance of my class is created,
    # the variable is incremented by 1.
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle attributes


        Args:
            width (int): Decribes the width of a rectangle
            height (int): Describes the height of a rectangle


        Returns:
            None
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Deletes the Rectangle objects


        Prints the message 'Bye rectangle...'
        """
        print("Bye rectangle...")
        # Here, every time an instance of my class is deleted,
        # the variable is decremented by 1.
        Rectangle.number_of_instances -= 1

    def area(self):
        """Calculates area of a rectangle


        Returns:
            the rectangle area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter of a rectangle


        Returns:
            the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    @property
    def width(self):
        """getting the width


        Returns:
            the width of a rectangle
        """
        return(self.__width)

    @property
    def height(self):
        """getting the height


        Returns:
            the height of a rectangle
        """
        return(self.__height)

    @width.setter
    def width(self, value):
        """setting the width


        Args:
            value (int):Describes the width of a rectangle


        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setting the height


        Args:
            value (int):Describes the height of a rectangle


        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        """Represents the Rectangle objects as a string


        Returns:
            the 'informal' representing string
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for i in range(self.__height))
        return(string)

    def __repr__(self):
        """Represents the Rectangle objects as a string


        Returns:
            the 'official' representing string
            to be able to recreate a new instance by using eval()
        """
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

# Private instance attribute: width:
# ...
# Private instance attribute: height:
# ...
# Public class attribute number_of_instances:
# Initialized to 0
# Incremented during each new instance instantiation
# Decremented during each instance deletion
# ...
