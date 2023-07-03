#!/usr/bin/python3
"""
This is a module containing the class for a rectangle.

It contains the getter and setter for the class also
"""


class Rectangle:
    """
    This lays a template for the object to be created
    """

    def __init__(self, width=0, height=0):
        """This initializes the ability to give paramaters"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """This is the width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is the width setter"""
        if type(value) != int or type(value) is None:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This is the height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is the height setter"""
        if type(value) != int or type(value) is None:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
