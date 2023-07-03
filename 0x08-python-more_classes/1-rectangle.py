#!/usr/bin/python3
"""
This is a module containing the class for a rectangle.

It contains nothing except pass
"""


class Rectangle:
    """
    This is an empty class containing nothing but the pass
    command to enable it throw no error
    """
    
    def __init__(self, width=0, height=0):
        height(height)
        width(width)
        
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
