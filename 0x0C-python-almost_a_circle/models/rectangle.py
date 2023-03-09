#!/usr/bin/python3
"""A  class Rectangle that inherits from Base."""
from models.base import Base


# Private instance attributes, each with its own public getter and setter:
# __width -> width
# __height -> height
# __x -> x
# __y -> y
class Rectangle(Base):
    """Module of a rectangle


    Attributes:
        id (int): Describes the identity of each instance
        __width (int): Decribes the width of a rectangle
        __height (int): Describes the height of a rectangle
        __x (int): Describes the x position
        __y (int): Describes the y position
    """
    # Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle attributes


        Args:
            id (int): Describes the identity of each instance
            width (int): Decribes the width of a rectangle
            height (int): Describes the height of a rectangle
            x (int): Describes the x position
            y (int): Describes the y position


        Returns:
            None
        """
        # Assign each argument width, height, x and y to the right attribute
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # Call the super class with id - this super call will use the logic of
        # the __init__ of the Base class
        super().__init__(id)

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

    @property
    def x(self):
        """getting x


        Returns:
            the x position
        """
        return(self.__x)

    @property
    def y(self):
        """getting y


        Returns:
            the y position
        """
        return(self.__y)

    # Validation of all setter methods and instantiation (id excluded):
    # If the input is not an integer, raise the TypeError exception with
    # the message: <name of the attribute> must be an integer. Example:
    # width must be an integer
    # If width or height is under or equals 0, raise the ValueError
    # exception with the message: <name of the attribute> must be > 0.
    # Example: width must be > 0
    # If x or y is under 0, raise the ValueError exception with the message:
    # <name of the attribute> must be >= 0. Example: x must be >= 0
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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setting x


        Args:
            value (int):Describes the x position


        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setting y


        Args:
            value (int):Describes the y position


        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # Public method def area(self): that returns the area value of the
    # Rectangle instance.
    def area(self):
        """Calculates area of a rectangle


        Returns:
            the rectangle area
        """
        return(self.__width * self.__height)

    # Public method def display(self): to print in stdout the Rectangle
    # instance with the character # by taking care of x and y
    def display(self):
        """Prints in stdout the Rectangle instance with the character #


        Returns:
            None
        """
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    # overriding the __str__ method so that it returns
    # [Rectangle] (<id>) <x>/<y> - <width>/<height>
    def __str__(self):
        """Represents the Rectangle objects as a string


        Returns:
            the 'informal' representing string
        """
        a, b, c = self.id, self.x, self.y
        d, e = self.width, self.height
        return("[Rectangle] ({}) {}/{} - {}/{}".format(a, b, c, d, e))

    # Public method def update(self, *args, **kwargs): that assigns a key/value
    # argument to attributes:
    # **kwargs can be thought of as a double pointer to a dictionary: key/value
    # As Python doesn’t have pointers, **kwargs is not literally a double
    # pointer – describing it as such is just a way of explaining its
    # behavior in terms you’re already familiar with **kwargs must be
    # skipped if *args exists and is not empty
    # Each key in this dictionary represents an attribute to the instance
    def update(self, *args, **kwargs):
        """ 'def update(self, *args):' alone assigns an argument to each
        attribute 'def update(self, *args, **kwargs):' assigns a key/value
        argument to attributes


        Args:
            args(list): no-keyword argument, order is important
            kwargs(dict): key-worded argument, order is not important

        Returns:
            None
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                # 1st argument should be the id attribute
                if i == 0:
                    self.id = arg
                # 2nd argument should be the width attribute
                elif i == 1:
                    self.width = arg
                # 3rd argument should be the height attribute
                elif i == 2:
                    self.height = arg
                # 4th argument should be the x attribute
                elif i == 3:
                    self.x = arg
                # 5th argument should be the y attribute
                elif i == 4:
                    self.y = arg

        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    # Public method def to_dictionary(self): that returns the dictionary
    # representation of a Rectangle
    # This dictionary must contain: id, width, height, x, y
    def to_dictionary(self):
        """
        Return:
            the dictionary representation of a Rectangle
        """
        return({"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y})
