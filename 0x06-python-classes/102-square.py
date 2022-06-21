#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (f"{self.__size*self.__size}")

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __gt__(self, other):
        return self.size > other.size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int or type(value) is not float:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
