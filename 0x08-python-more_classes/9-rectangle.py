#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""


# Instance Methods
# You can see the method takes one parameter, self, which points to an instance
# of my class when the method is called (but of course instance methods can
# accept more than just one parameter).
# Through the self parameter, instance methods can freely access attributes and
# other methods on the same object. This gives them a lot of power when it
# comes to modifying an object’s state.
# Not only can they modify object state, instance methods can also access the
# class itself through the self.__class__ attribute. This means instance
# methods can also modify class state.
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

    # Class Methods
    # Instead of accepting a self parameter, class methods take a cls
    # parameter that points to the class—and not the object instance—when
    # the method is called.
    # Because the class method only has access to this cls argument, it
    # can’t modify object instance state. That would require access to
    # self. However, class methods can still modify class state that
    # applies across all instances of the class.
    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

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
# Class method def square(cls, size=0): that returns a new Rectangle
# instance with width == height == size
