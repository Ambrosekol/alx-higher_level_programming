#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import sys as system
from io import StringIO


class TestBaseClass(unittest.TestCase):
    """
    This tests the base class and makes sure everything works the way
    it should
    """

    def test_initVal_without_args(self):
        newInst = Base()
        self.assertEqual(newInst.id, 1)

    def test_initVal_with_arg(self):
        newInst = Base(121)
        self.assertEqual(newInst.id, 121)

    def test_to_json_string(self):
        testItem = {
            'x': 2,
            'width': 10,
            'id': 1,
            'height': 7,
            'y': 8
            }
        resp = Base.to_json_string(testItem)
        self.assertEqual(resp, str([]))
        newresp = Base.to_json_string(list(testItem))
        self.assertTrue(type(newresp) == str)

    def test_save_to_file(self):
        Square.save_to_file([Square(10, 2, 3, 20), Square(1, 4, 6, 80)])
        with open("Square.json", mode="r") as file:
            ioInstance = StringIO()
            system.stdout = ioInstance
            print(file.read())
            output = ioInstance.getvalue()
            system.stdout = system.__stdout__
            testValues = "[{\"id\": 20, \"size\": 10, \"x\": 2, \"y\": 3\
}, {\"id\": 80, \"size\": 1, \"x\": 4, \"y\": 6}]\n"
            self.assertEqual(output, testValues)
