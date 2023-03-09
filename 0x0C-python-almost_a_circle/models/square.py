#!/usr/bin/python3
"""A  class Square that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Module of a square


    Use all attributes of Rectangle
    """
    # Class constructor: def __init__(self, size, x=0, y=0, id=None):
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the rectangle attributes


        Args:
            id (int): Describes the identity of each instance
            x (int): Describes the x position
            y (int): Describes the y position
            size(int): Describes the length of a square

        Returns:
            None
        """
        # Call the super class with id, x, y, width and height - this super
        # call will use the logic of the __init__ of the Rectangle class.
        # The width and height must be assigned to the value of size
        # You must not create new attributes for this class, use all
        # attributes of Rectangle - As reminder: a Square is a
        # Rectangle with the same width and height
        # All width, height, x and y validation must inherit from Rectangle
        # - same behavior in case of wrong data
        super().__init__(size, size, x, y, id)
        self.size = size

    # public getter and setter size
    # The setter should assign (in this order) the width and the height - with
    # the same value
    # The setter should have the same value validation as the Rectangle for
    # width and height - No need to change the exception error message (It
    # should be the one from width)
    @property
    def size(self):
        """getting the size


        Returns:
            the length of a square
        """
        return(self.width)

    """The width and height must be assigned to the value of size"""
    @size.setter
    def size(self, value):
        """setting the size


        Args:
            value (int):Describes the length of a square


        Returns:
            None
        """
        self.width = value
        self.height = value

    # The overloading __str__ method should return
    # [Square] (<id>) <x>/<y> - <size> - in our case, width or height
    def __str__(self):
        """Represents the Square objects as a string


        Returns:
            the 'informal' representing string
        """
        a, b, c = self.id, self.x, self.y
        d = self.width
        return("[Square] ({}) {}/{} - {}".format(a, b, c, d))

    # Public method def update(self, *args, **kwargs) that assigns attributes:
    # *args is the list of arguments - no-keyworded arguments
    # **kwargs can be thought of as a double pointer to a dictionary: key/value
    # (keyworded arguments)
    # **kwargs must be skipped if *args exists and is not empty
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
                # 2nd argument should be the size attribute
                elif i == 1:
                    self.size = arg
                # 3rd argument should be the x attribute
                elif i == 2:
                    self.x = arg
                # 4th argument should be the y attribute
                elif i == 3:
                    self.y = arg

        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    # Public method def to_dictionary(self): that returns the dictionary
    # representation of a Square:
    # This dictionary must contain: id, size, x, y
    def to_dictionary(self):
        """
        Return:
            the dictionary representation of a Square
        """
        return({"id": self.id, "size": self.size, "x": self.x, "y": self.y})
