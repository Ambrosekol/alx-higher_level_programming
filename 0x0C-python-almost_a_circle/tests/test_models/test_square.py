#!/usr/bin/python3
from models.square import Square
import unittest
import sys as system
from io import StringIO


"""
This file contains the unitest test for the Square class.
It tests all functions and cases for the File
"""


class TestSquareClass(unittest.TestCase):
    """
    The begining of unit test for the square
    """
    
    def test_init_method(self):
        newlocalInst = Square(2, id=4)
        self.assertEqual(newlocalInst.height, 2)
        self.assertEqual(newlocalInst.width, 2)
        self.assertEqual(newlocalInst.id == 4, True)

    def test_display_representation(self):
        newlocalInst = Square(3, id=4)
        strngIO = StringIO()
        system.stdout = strngIO
        newlocalInst.display()
        output = strngIO.getvalue()
        system.stdout = system.__stdout__
        expectedOutput = "###\n###\n###\n"
        self.assertEqual(output, expectedOutput)

    def test_str_representataion(self):
        newlocalInst = Square(2)
        self.assertTrue(str(newlocalInst) == "[Square] (8) 0/0 - 2", True)
    
    def test_area(self):
        newlocalInst = Square(10)
        area = newlocalInst.area()
        self.assertEqual(area, 100)