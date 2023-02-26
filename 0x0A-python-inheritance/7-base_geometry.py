#!/usr/bin/python3
"""An class BaseGeometry that defines a base"""


class BaseGeometry:
    """Module of a base"""
    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value to be integer and greater than 0"""
        # condition to check whether 'value' is suitable or not
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

# A class BaseGeometry (based on 6-base_geometry.py).
# Public instance method: def area(self): that raises an Exception with
# the message area() is not implemented
# Public instance method: def integer_validator(self, name, value): that
# validates value:
# you can assume name is always a string
# if value is not an integer: raise a TypeError exception, with the message
# <name> must be an integer
# if value is less or equal to 0: raise a ValueError exception with the
# message <name> must be greater than 0
