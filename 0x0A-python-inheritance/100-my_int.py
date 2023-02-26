#!/usr/bin/python3
"""
A class MyInt that inherits from int
"""


# To run the first step,Python classes have a special method called .__new__(),
# which is responsible for creating and returning a new empty object. Then
# another special method, .__init__(), takes the resulting object, along
# with the class constructor’s arguments.
# The .__init__() method takes the new object as its first argument, self. Then
# it sets any required instance attribute to a valid state using the arguments
# that the class constructor passed to it.
# In short, Python’s instantiation process starts with a call to the
# class constructor, which triggers the instance creator, .__new__(),
# to create a new empty object. The process continues with the instance
# initializer, .__init__(), which takes the constructor’s arguments to
# initialize the newly created object.
# def __new__(cls, *args, **kwargs) is a special method in Python that
# is used to create a new instance of a class. It is called before the
# __init__() method and is responsible for creating and returning a new
# object of the class.
# The cls parameter represents the class that __new__() is called on. It
# is automatically passed as the first parameter when __new__() is called,
# and you should always include it as the first parameter in the method
# definition.
# The *args parameter represents any positional arguments that may be passed
# to __new__(). These arguments are passed as a tuple, and you can access
# them inside the method using indexing, like you would with any other tuple.
# The **kwargs parameter represents any keyword arguments that may be passed
# to __new__(). These arguments are passed as a dictionary, and you can access
# them inside the method using keys, like you would with any other dictionary.
class MyInt(int):
    """Module of a rebel"""
    def __new__(cls, *args, **kwargs):
        """creates object inside __new__ method by using super"""
        # return(super(MyInt, cls).__new__(cls, *args, **kwargs)) is a
        # Python statement statement that calls the __new__() method of
        # the parent class of MyInt class, passing cls (i.e., MyInt) as
        # the first parameter along with any additional positional and
        # keyword arguments that are passed to __new__(). This is
        # typically used in a subclass to create a new instance of the
        # subclass by delegating the creation of the object to its
        # parent class.
        # This statement is used to create a new instance of the MyInt
        # class, while also inheriting the behavior of the int class.
        # The super() function is used to get a reference to the superclass,
        # and the .__new__(cls) method is called on it to create a new object
        # of the superclass. The cls parameter is passed to the method to
        # indicate that the object should be created as an instance of the
        # current class (rather than the superclass).
        return(super(MyInt, cls).__new__(cls, *args, **kwargs))

    # The implementation of the __eq__() method you provided compares the
    # integer value of self with the value of other and returns True if
    # they are not equal, and False otherwise. Which means that the two
    # objects are considered "equal" when they have different integer
    # values. This is achieved using the int() function to convert self
    # to an integer and then comparing it with other.
    def __eq__(self, other):
        """!= inverted to =="""
        return(int(self) != other)

    # The implementation of the __ne__() method you provided compares the
    # integer value of self with the value of other and returns True if
    # they are equal, and False otherwise. Which means that the two
    # objects are considered "not equal" when they have similar integer
    # values. This is achieved using the int() function to convert self
    # to an integer and then comparing it with other.
    def __ne__(self, other):
        """== inverted to !="""
        return(int(self) == other)

# A class MyInt that inherits from int:
# MyInt is a rebel. MyInt has == and != operators inverted
