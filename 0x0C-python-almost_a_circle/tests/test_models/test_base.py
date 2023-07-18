#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import sys as system
from io import StringIO
import os


class TestBaseClass(unittest.TestCase):
    """
    This tests the base class and makes sure everything works the way
    it should
    """

    def test_initVal_without_args(self):
        """
        Tests the init value for Base class without args
        """
        newInst = Base()
        self.assertEqual(newInst.id, 2)

    def test_initVal_with_arg(self):
        """
        Tests the init value for Base class with args
        """
        newInst = Base(121)
        self.assertEqual(newInst.id, 121)

    def test_to_json_string(self):
        """
        Tests from object to json string
        """
        testItem = {
            'x': 2,
            'width': 10,
            'id': 1,
            'height': 7,
            'y': 8
            }
        resp = Base.to_json_string(testItem)
        self.assertEqual(resp, str([]))
        newresp = Base.to_json_string([testItem])
        self.assertTrue(type(newresp) == str)

    def test_save_to_file(self):
        """
        Tests save to file
        """
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

    def test_from_json_string(self):
        """
        Tests from json String
        """
        input1 = [
            {
                'id': 89,
                'width': 10,
                'height': 4
                },
            {
                'id': 7,
                'width': 1,
                'height': 7
                }
            ]
        input2 = []
        stringrepr = Base.to_json_string(input1)
        stringrepr2 = Base.to_json_string(input2)
        TestVal = Base.from_json_string(stringrepr)
        TestVal2 = Base.from_json_string(stringrepr2)
        self.assertTrue(input1 == TestVal)
        self.assertTrue(input2 == TestVal2)

    def test_create_rectangle(self):
        """
        Tests to create a Rectangle
        """
        rectangle_dict = {'id': 1, 'width': 5, 'height': 3, 'x': 2, 'y': 4}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.id, rectangle_dict['id'])
        self.assertEqual(rectangle.width, rectangle_dict['width'])
        self.assertEqual(rectangle.height, rectangle_dict['height'])
        self.assertEqual(rectangle.x, rectangle_dict['x'])
        self.assertEqual(rectangle.y, rectangle_dict['y'])

    def test_load_from_file(self):
        """
        Tests to load from file
        """
        r1 = Rectangle(10, 5)
        r2 = Rectangle(7, 3)
        s1 = Square(4)
        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1])
        rectangles = Rectangle.load_from_file()
        squares = Square.load_from_file()

        self.assertEqual(len(rectangles), 2)
        self.assertEqual(len(squares), 1)

        self.assertEqual(rectangles[0].id, 3)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[0].height, 5)
        self.assertEqual(rectangles[1].id, 4)
        self.assertEqual(rectangles[1].width, 7)
        self.assertEqual(rectangles[1].height, 3)
        self.assertEqual(squares[0].id, 5)
        self.assertEqual(squares[0].size, 4)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)