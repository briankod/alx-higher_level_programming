#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


class Rectangle:
    """Module of a rectangle


    Attributes:
        __width (int): Decribes the width of a rectangle
        __height (int): Describes the height of a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances -= 1

    def area(self):
        """Calculates area of a rectangle


        Returns:
            the rectangle area
        """
        return(self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter of a rectangle


        Returns:
            the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return((self.__width * 2) + (self.__height * 2))

    # Static Methods
    # @staticmethod is a decorator, that gives the decorated method a static
    # behavior. A decorator is simply a wrapper using the syntactic sugar “@”.
    # This type of method takes neither a self nor a cls parameter (but of
    # course it’s free to accept an arbitrary number of other parameters).
    # Therefore a static method can neither modify object state nor class
    # state. Static methods are restricted in what data they can
    # access - and they’re primarily a way to namespace your methods.
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles using their areas


        Args:
            rect_1 (int): Describes the first rectangle for comparison
            rect_2 (int): Describes the second rectangle for comparison


        Returns:
            the biggest rectangle based on the area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        else:
            return(rect_2)

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
            string += "\n".join(str(self.print_symbol) * self.__width
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
# Static method def bigger_or_equal(rect_1, rect_2): that returns the
# biggest rectangle based on the area
# rect_1 must be an instance of Rectangle, otherwise raise a TypeError
# exception with the message 'rect_1 must be an instance of Rectangle'
# rect_2 must be an instance of Rectangle, otherwise raise a TypeError
# exception with the message 'rect_2 must be an instance of Rectangle'
# Returns rect_1 if both have the same area value
