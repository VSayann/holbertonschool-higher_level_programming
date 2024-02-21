#!/usr/bin/python3
"""Test case for the base module"""
import unittest
from models.base import Base


class Test_class_Base(unittest.TestCase):
    """Test for the class Base"""
    def test_id_int(self):
        """id is a number"""
        cls_B = Base(10)
        self.assertEqual(10, cls_B.id)

    def test_id_negative(self):
        """id is a negative number"""
        cls_B = Base(-10)
        self.assertEqual(-10, cls_B.id)

    def test_id_zero(self):
        """id is zero"""
        cls_B = Base(0)
        self.assertEqual(0, cls_B.id)

    def test_id_None(self):
        """id is None"""
        cls_B = Base(None)
        self.assertEqual(1, cls_B.id)

    def test_id_string(self):
        """id is a string"""
        cls_B = Base("string")
        self.assertEqual("string", cls_B.id)

    def test_id_character(self):
        """id is a character"""
        cls_B = Base("a")
        self.assertEqual("a", cls_B.id)

    def test_id_float(self):
        """id is a float number"""
        cls_B = Base(5.2)
        self.assertEqual(5.2, cls_B.id)

    def test_id_list(self):
        """id is a list"""
        cls_B = Base([1, 2])
        self.assertEqual([1, 2], cls_B.id)

    def test_id_matrix(self):
        """id is a matrix"""
        cls_B = Base([[1, 2], [3, 4]])
        self.assertEqual([[1, 2], [3, 4]], cls_B.id)

    def test_id_tuple(self):
        """id is a tuple"""
        cls_B = Base((1, 2))
        self.assertEqual((1, 2), cls_B.id)

    def test_id_dictionary(self):
        """id is integer"""
        cls_B = Base({"id": 10})
        self.assertEqual({"id": 10}, cls_B.id)

    def test_id_empty(self):
        """id is empty"""
        cls_B = Base()
        self.assertEqual(2, cls_B.id)
