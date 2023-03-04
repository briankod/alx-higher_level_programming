#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """Module of a student


    Attributes:
        first_name (str): Describes the 1st name of a student
        last_name (str): Describes the last name of a student
        age (int): Describes the age of a student
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the student attributes


        Args:
            first_name (str): Describes the 1st name of a student
            last_name (str): Describes the last name of a student
            age (int): Describes the age of a student


        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # The method below takes an optional list of attribute names (attrs) and
    # returns a dictionary representation of the object with only the
    # attributes specified in attrs.
    # hasattr() function returns True if the specified object has the specified
    # attribute, otherwise False.
    # Syntax:  hasattr(object, attribute)
    # getattr() function returns the value of the specified attribute from the
    # specified object.
    # Syntax:  getattr(object, attribute, default)
    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        # It checks if attrs is None. If it is, it returns the dictionary
        # representation of the entire object (self.__dict__).
        if attrs is None:
            return(self.__dict__)
        # If attrs is not None, it creates a new empty dictionary new_dict.
        new_dict = {}
        # It loops through each element in attrs. For each element, it checks
        # if the object (self) has an attribute with that name using the
        # built-in hasattr() function.
        for elm in attrs:
            if hasattr(self, elm):
                # If the object has the attribute, it gets the attribute value
                # using the built-in getattr() function and adds it to the new
                # dictionary with the same name as the attribute.
                new_dict[elm] = getattr(self, elm)
        # Finally, it returns the new dictionary containing only the attributes
        # specified in attrs.
        return(new_dict)

# A class Student that defines a student by: (based on 9-student.py)
# Public instance attributes:
# ...
# Public method def to_json(self, attrs=None): that retrieves a dictionary
# representation of a Student instance (same as 8-class_to_json.py):
# If attrs is a list of strings, only attribute names contained in this list
# must be retrieved. Otherwise, all attributes must be retrieved
