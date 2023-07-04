#!/usr/bin/python3
"""
This is a module containing the class for a rectangle.

It contains the getter and setter for the class also
"""


class Rectangle:
    """
    This lays a template for the object to be created
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height
            Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__height > 0 and self.__width > 0:
            rect = ""
            for val in range(self.__height):
                rect += Rectangle.print_symbol\
                        * self.__width + "\n"
            return rect
        else:
            return ""

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ","\
            + str(self.__height) + ")"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        peri = 2 * (self.__width + self.__height)
        return peri
