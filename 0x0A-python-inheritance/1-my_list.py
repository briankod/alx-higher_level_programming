#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


# In Python, super().__init__() is a method call that allows a subclass
# to call the __init__() method of its superclass.
# When you create a subclass, you may want to inherit the attributes
# and methods of the parent class, but you may also want to add some
# additional attributes or behavior specific to the subclass.
# In order to do this, you can call the parent class's __init__() method
# using super().__init__(param1, param2, ...), which will initialize the
# attributes inherited from the parent class.
class MyList(list):
    """Derived class of super class list"""
    def __init__(self):
        """initializes the object's attributes"""
        super().__init__()
        """Calls the initialization method of the super class list"""

    # The sorted() function sorts the elements of a given iterable in a
    # specific order (ascending or descending) and returns it as a list.
    # Syntax:
    # sorted(iterable, key=None, reverse=False)
    def print_sorted(self):
        """prints the sorted list (ascending sort)"""
        print(sorted(self))

# A class MyList that inherits from list
