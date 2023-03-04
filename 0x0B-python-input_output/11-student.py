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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return(self.__dict__)
        new_dict = {}
        for elm in attrs:
            if hasattr(self, elm):
                new_dict[elm] = getattr(self, elm)
        return(new_dict)

    # The reload_from_json method takes in a dictionary json and assigns
    # each key-value pair in the dictionary to an attribute in the object
    # that calls the method.
    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        # The method iterates through each element elm in the json dictionary
        # using a for loop. For each elm, the method accesses the object's
        # __dict__ attribute, which contains a dictionary of the object's
        # attributes and their values, and assigns the value of json[elm]
        # to the object's attribute with the same name as elm.
        for elm in json:
            self.__dict__[elm] = json[elm]

# A class Student that defines a student by: (based on 10-student.py)
# Public instance attributes:
# ...
# Public method def reload_from_json(self, json): that replaces all
# attributes of the Student instance:
# You can assume json will always be a dictionary
# A dictionary key will be the public attribute name
# A dictionary value will be the value of the public attribute
