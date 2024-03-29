#!/usr/bin/python3
"""A class Base that defines a base of all other classes."""
import json
import csv
import turtle


class Base:
    """Module of a base


    Attributes:
        id (int): Describes the identity of each instance
        __nb_objects (int): Describes the number of instances of our class
    """
    # private class attribute __nb_objects = 0
    __nb_objects = 0

    # class constructor: def __init__(self, id=None):
    def __init__(self, id=None):
        """Initializes the base attributes


        Args:
          id (int): Describes the identity of each instance

        Returns:
            None
        """
        # if id is not None, assign the public instance attribute id with
        # this argument value - you can assume id is an integer and you
        # don’t need to test the type of it
        if id is not None:
            self.id = id
        # otherwise, increment __nb_objects and assign the new value to the
        # public instance attribute id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # static method def to_json_string(list_dictionaries): that returns the
    # JSON string representation of list_dictionaries
    # list_dictionaries is a list of dictionaries
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        # If list_dictionaries is None or empty, return the string: "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        # Otherwise, return the JSON string representation of list_dictionaries
        return(json.dumps(list_dictionaries))

    # static method def from_json_string(json_string): that returns the list of
    # the JSON string representation json_string
    # json_string is a string representing a list of dictionaries
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        # If json_string is None or empty, return an empty list
        if json_string is None or len(json_string) == 0:
            return []
        # Otherwise, return the list represented by json_string
        return(json.loads(json_string))

    # class method def save_to_file(cls, list_objs):that writes the JSON string
    # representation of list_objs to a file
    # list_objs is a list of instances who inherits of Base - example: list of
    # Rectangle or list of Square instances
    # If list_objs is None, save an empty list
    # You must use the static method to_json_string (created before)
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        # The filename must be: <Class name>.json - example: Rectangle.json
        filename = cls.__name__ + ".json"
        my_obj = []
        if list_objs is not None:
            for elm in list_objs:
                my_obj.append(cls.to_dictionary(elm))
        with open(filename, 'w') as f:
            # You must overwrite the file if it already exists
            f.write(cls.to_json_string(my_obj))

    # class method def create(cls, **dictionary): that returns an instance with
    # all attributes already set
    # **dictionary can be thought of as a double pointer to a dictionary
    # To use the update method to assign all attributes, you must create a
    # “dummy” instance before:
    # Create a Rectangle or Square instance with “dummy” mandatory attributes
    # (width, height, size, etc.)
    # Call update instance method to this “dummy” instance to apply your real
    # values
    # You must use the method def update(self, *args, **kwargs)
    # **dictionary must be used as **kwargs of the method update
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return(dummy)

    # class method def load_from_file(cls): that returns a list of instances
    # The filename must be: <Class name>.json - example: Rectangle.json
    # If the file doesn’t exist, return an empty list
    # Otherwise, return a list of instances - the type of these instances
    # depends on cls (current class using this method)
    # You must use the from_json_string and create methods (implemented
    # previously)
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        my_obj = []
        try:
            with open(filename, 'r') as file:
                my_obj = cls.from_json_string(file.read())
            for i, elm in enumerate(my_obj):
                my_obj[i] = cls.create(**my_obj[i])
        except (Exception):
            pass
        return(my_obj)

    # class methods def save_to_file_csv(cls, list_objs): and
    # def load_from_file_csv(cls):
    # that serializes and deserializes in CSV:
    # The filename must be: <Class name>.csv - example: Rectangle.csv
    # Has the same behavior as the JSON serialization/deserialization
    # Format of the CSV:
    # Rectangle: <id>,<width>,<height>,<x>,<y>
    # Square: <id>,<size>,<x>,<y>
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of rectangles or squares in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for elm in list_objs:
                    writer.writerow([elm.id, elm.width, elm.height,
                                     elm.x, elm.y])
            elif cls.__name__ == "Square":
                for elm in list_objs:
                    writer.writerow([elm.id, elm.size, elm.x, elm.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of rectanglesor squares in csv"""
        filename = cls.__name__ + ".csv"
        my_obj = []
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f)
                for elm in csv_reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(elm[0]), "width": int(elm[1]),
                                      "height": int(elm[2]), "x": int(elm[3]),
                                      "y": int(elm[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(elm[0]), "size": int(elm[1]),
                                      "x": int(elm[2]), "y": int(elm[3])}
                    obj = cls.create(**dictionary)
                    my_obj.append(obj)
        except(Exception):
            pass
        return(my_obj)

    # static method def draw(list_rectangles, list_squares): that opens a
    # window and draws all the Rectangles and Squares:
    # You must use the Turtle graphics module
    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        window = turtle.Screen()
        turtle.speed(5)
        turtle.pensize(5)
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.color("black")
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for colors in ["red", "yellow", "purple", "blue"]:
                turtle.color(colors)
                turtle.forward(square.size)
                turtle.left(90)
        turtle.penup()

        window.exitonclick()
