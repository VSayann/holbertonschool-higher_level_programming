#!/usr/bin/python3
"""Test case for module rectangle"""

import unittest
import sys
from io import StringIO
from tests.test_models.test_base import Test_class_Base
from models.rectangle import Rectangle


class Test_class_Rectangle(Test_class_Base):
    """Test for the class Rectangle"""
    def test_id_is_None(self):
        """adapt the test for class rectangle"""
        cls_R = Rectangle(20, 10)
        self.assertEqual(13, cls_R.id)

    def test_width_setter(self):
        """test the setter method of width"""
        cls_R = Rectangle(20, 10)
        cls_R.width = 25
        self.assertEqual(25, cls_R.width)

    def test_height_setter(self):
        """test the setter method of height"""
        cls_R = Rectangle(20, 10)
        cls_R.height = 8
        self.assertEqual(8, cls_R.height)

    def test_x_setter(self):
        """test the setter method of x"""
        cls_R = Rectangle(20, 10)
        cls_R.x = 25
        self.assertEqual(25, cls_R.x)

    def test_y_setter(self):
        """test the setter method of y"""
        cls_R = Rectangle(20, 10)
        cls_R.y = 8
        self.assertEqual(8, cls_R.y)

    """--------------------TEST WIDTH TYPE--------------------"""

    def test_width_string(self):
        """test if width is a string"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle("string", 10)

    def test_width_character(self):
        """test if width is a character"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle("a", 10)

    def test_width_float(self):
        """test if width is a float"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle("3.5", 10)

    def test_width_list(self):
        """test if width is a list"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle([1, 2], 10)

    def test_width_tuple(self):
        """test if width is a tuple"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle((1, 2), 10)

    def test_width_matrix(self):
        """test if width is a matrix"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle([[1, 2], [3, 4]], 10)

    def test_width_dicitonary(self):
        """test if width is a dictionary"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle({"width": 20}, 10)

    def test_width_negative_int(self):
        """test if width is a negative number"""
        with self.assertRaises(ValueError):
            cls_R = Rectangle(-5, 10)

    """--------------------TEST HEIGHT TYPE--------------------"""

    def test_height_string(self):
        """test if height is a string"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(10, "string")

    def test_height_character(self):
        """test if height is a character"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, "a")

    def test_height_float(self):
        """test if height is a float"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10.5)

    def test_height_list(self):
        """test if height is a list"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, [1, 2])

    def test_height_tuple(self):
        """test if height is a tuple"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, (1, 2))

    def test_height_matrix(self):
        """test if height is a matrix"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, [[1, 2], [3, 4]])

    def test_height_dicitonary(self):
        """test if height is a dictionary"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, {"heigth": 10})

    def test_height_negative_int(self):
        """test if height is a negative number"""
        with self.assertRaises(ValueError):
            cls_R = Rectangle(20, -5)

    """--------------------TEST X TYPE--------------------"""

    def test_x_string(self):
        """test if x is a string"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, "string")

    def test_x_character(self):
        """test if x is a character"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, "a")

    def test_x_float(self):
        """test if x is a float"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, 20.5)

    def test_x_list(self):
        """test if x is a list"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, [1, 2])

    def test_x_tuple(self):
        """test if x is a tuple"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, (1, 2))

    def test_x_matrix(self):
        """test if x is a matrix"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, [[1, 2], [3, 4]])

    def test_x_dicitonary(self):
        """test if x is a dictionary"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, {"x": 20})

    def test_x_negative_int(self):
        """test if x is a negative number"""
        with self.assertRaises(ValueError):
            cls_R = Rectangle(20, 10, -5)

    """--------------------TEST Y TYPE--------------------"""

    def test_y_string(self):
        """test if width is a string"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, 20, "string")

    def test_y_character(self):
        """test if y is a character"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, 20, "a")

    def test_y_float(self):
        """test if y is a float"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, 20, 10.5)

    def test_y_list(self):
        """test if y is a list"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, 20, [1, 2])

    def test_y_tuple(self):
        """test if y is a tuple"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, 20, (1, 2))

    def test_y_matrix(self):
        """test if y is a matrix"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, 20, [[1, 2], [3, 4]])

    def test_y_dicitonary(self):
        """test if y is a dictionary"""
        with self.assertRaises(TypeError):
            cls_R = Rectangle(20, 10, 20, {"y": 20})

    def test_y_negative_int(self):
        """test if y is a negative number"""
        with self.assertRaises(ValueError):
            cls_R = Rectangle(20, 10, 20, -10)

    """--------------------TEST DIFFERENT METHODS--------------------"""

    def test_area(self):
        """test the method area"""
        cls_R = Rectangle(20, 10)
        self.assertEqual(200, cls_R.area())

    def test_display(self):
        """test the method for display the rectangle"""
        cls_R = Rectangle(5, 2)

        with StringIO() as output:
            sys.stdout = output
            cls_R.display()
            printed_output = output.getvalue()

        sys.stdout = sys.__stdout__
        self.assertEqual("#####\n#####\n", printed_output)


if __name__ == "__main__":
    unittest.main()
