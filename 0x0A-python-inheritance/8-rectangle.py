#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry
"""
# The __import__() in python module helps in getting the code present in
# another module by either importing the function or code or file using
# the import in python method.
# Syntax:
# __import__(name, globals=None, locals=None, fromlist=(), level=0)
# name - the name of the module you want to import
# globals and locals - determines how to interpret name
# fromlist - objects or submodules that should be imported by name
# level - specifies whether to use absolute or relative imports
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Module of a rectangle"""
    def __init__(self, width, height):
        """Initializes the rectangle attributes"""
        # condition to check whether 'width' is suitable or not
        self.integer_validator("width", width)
        self.__width = width
        # condition to check whether 'height' is suitable or not
        self.integer_validator("height", height)
        self.__height = height

# A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
# Instantiation with width and height: def __init__(self, width, height):
# width and height must be private. No getter or setter
# width and height must be positive integers, validated by integer_validator
