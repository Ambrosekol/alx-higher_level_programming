#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest


"""
This file contains the test file for the rectangle class
"""


class RectangleTestClass(unittest.TestCase):
    """
    This is the class that performs the test
    """

    newInst = Rectangle(10, 5, 4, 5)

    def test_input_for_rectangle(self):
        """
        This tests the input for rectangle class
        """
        self.assertEqual(RectangleTestClass.newInst.id, 1)

    def test_setter_for_rectangle(self):
        localval = RectangleTestClass.newInst
        newval_h = 3
        newval_w = 2
        newval_x = 0
        newval_y = 0
        localval.width = newval_w
        localval.height = newval_h
        localval.x = newval_x
        localval.y = newval_y
        self.assertEqual(localval.height, newval_h)
        self.assertEqual(localval.width, newval_w)
        self.assertEqual(localval.x, newval_x)
        self.assertEqual(localval.y, newval_y)

    def test_newInstanc(self):
        localNewInst = Rectangle(10, 34, id=9)
        self.assertEqual(localNewInst.id, 9)

    def test_wrong_type(self):
        localinst = RectangleTestClass.newInst
        wrngTyp = "3"
        wrngVal = -1
        noneVal = None
        with self.assertRaises(TypeError):
            localinst.width = wrngTyp
            localinst.height = wrngTyp
            localinst.x = wrngTyp
            localinst.y = wrngTyp

        with self.assertRaises(ValueError):
            localinst.width, localinst.height = (wrngVal, wrngVal)
            localinst.x, localinst.y = (wrngVal, wrngVal)

        with self.assertRaises(TypeError):
            localinst.height, localinst.width = (noneVal, noneVal)
            localinst.x, localinst.y = (noneVal, noneVal)

    def test_area_functionality(self):
        newLocalInst = Rectangle(90, 2, 0, 0, 1003)
        area = newLocalInst.area
        self.assertEqual(area, 1800)
        self.assertEqual(newLocalInst.id, 1003)
