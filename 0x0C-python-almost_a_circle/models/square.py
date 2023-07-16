#!/usr/bin/python3
from models.rectangle import Rectangle


"""
This is a module containing the code for the Square class.
"""


class Square(Rectangle):
    """
    The Square class inherits from the Rectangle class which then
    inherits from the Base class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return "[Square] ({}) {}/{} \
- {}".format(self.id, self.x, self.y,
                self.width)
