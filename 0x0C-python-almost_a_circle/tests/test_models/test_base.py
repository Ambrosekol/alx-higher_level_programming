#!/usr/bin/python3
import unittest
from models.base import Base


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
