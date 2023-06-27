#!/usr/bin/python3
"""
This is a module that creates a Square class with initialization of Square size
for ALX high level programming.
This is task 3 and that is all this module will handle
"""


class Square:
    """
    This now a Square class with the size initialization and also
    this checks if the size variable is an int or less than 0.

    A new public instance method caleed 'area' is added in order
    to calculate the area of a square.

    A new public instance method caleed 'my_print' is added in
    order to print the square to stdout
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """This calculates the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """This is the class property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """This is the class property setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the attribue named Position"""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int \
                or type(value[1]) != int or value[0] >= 0 or value[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
