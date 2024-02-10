"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test class for module max_integer"""
    def test_int(self):
        """test with int"""
        test_list = [1, 2, 3, 4, 5, 6]
        result = max_integer(test_list)
        self.assertEqual(result, 6)

    def test_float(self):
        """test with float"""
        test_list = [0.5, 5.6, 9.8, 7.3]
        result = max_integer(test_list)
        self.assertEqual(result, 9.8)

    def test_negative_int(self):
        """test with negative numbers"""
        test_list = [-1, -2, -3, -4, -5, -6]
        result = max_integer(test_list)
        self.assertEqual(result, -1)

    def test_string(self):
        """test with string"""
        test_list = "test string"
        result = max_integer(test_list)
        self.assertEqual(result, "t")

    def test_characters(self):
        """test with characters"""
        test_list = ["a", "z", "c", "d"]
        result = max_integer(test_list)
        self.assertEqual(result, "z")

    def test_matrice(self):
        """test with matrice"""
        test_list = [[1, 2, 3], [4, 5, 6]]
        result = max_integer(test_list)
        self.assertEqual(result, [4, 5, 6])

    def test_boolean(self):
        """test a boolean"""
        test_list = [True, False]
        result = max_integer(test_list)
        self.assertEqual(result, True)

    def test_is_none(self):
        """test with list is none"""
        test_lit = [None]
        result = max_integer(test_lit)
        self.assertEqual(result, None)

    def test_same_value(self):
        """test with same values"""
        test_list = [5, 5, 5, 5, 5]
        result = max_integer(test_list)
        self.assertEqual(result, 5)

    def test_empty_list(self):
        """test empty list"""
        test_list = []
        result = max_integer(test_list)
        self.assertEqual(result, None)

    def test_one_value(self):
        """test with one value"""
        test_list = [3]
        result = max_integer(test_list)
        self.assertEqual(result, 3)

    def test_one_character(self):
        """test with one character"""
        test_list = "a"
        result = max_integer(test_list)
        self.assertEqual(result, "a")

    def test_none(self):
        """test with none"""
        self.assertRaises(TypeError, max_integer, None)

    def test_number_arguments(self):
        """test number of arguments of the function"""
        self.assertRaises(TypeError, max_integer, 1, 2, 3)

    def test_multiple_types(self):
        """test with multiple types"""
        self.assertRaises(TypeError, max_integer, ["a", 1, None, "test", 8.5])

    def test_dictionary(self):
        """test with a dictionary"""
        self.assertRaises(KeyError, max_integer, {"a": 1, "b": 2})


if __name__ == "__main__":
    unittest.main()