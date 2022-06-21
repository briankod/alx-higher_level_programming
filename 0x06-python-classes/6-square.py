#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return (f"{self.__size*self.__size}")

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for m in range(self.__position[0])]), end="")
            print("".join(["#" for n in range(self.__size)]))

    @property
    def size(self):
        return(self.__size)

    @property
    def position(self):
        return(self._position)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        err = "position must be a tuple of 2 positive integers"
        if type(value) is tuple:
            if len(value) == 2:
                a, b = value
                if a >= 0 or b >= 0:
                    self.__position = value
                else:
                    raise TypeError(err)
            else:
                raise TypeError(err)
        else:
            raise TypeError(err)
