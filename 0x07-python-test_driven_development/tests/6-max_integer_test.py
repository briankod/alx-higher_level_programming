#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Module of max_integer unittest"""
    def m_docstr_test(self):
        """Tests for module docsting"""
        m_docstr = __import__('6-max_integer').__doc__
        self.assertTrue(len(m_docstr) > 1)

    def f_docstr_test(self):
        """Tests for funstion docstring"""
        f_docstr = max_integer.__doc__
        self.assertTrue(len(f_docstr) > 1)

    def empty_list_test(self):
        """Tests for empty list"""
        lst = []
        self.assertIsNone(max_integer(lst))

    def test_no_args(self):
        """Tests for no arguments"""
        self.assertIsNone(max_integer())

    def identical_int_test(self):
        """Tests for all positive with max at end"""
        lst = [3, 4, 7, 3]
        self.assertEqual(max_integer(lst), 3)

    def not_int_test(self):
        """Tests for non-integers in list"""
        lst = [2, 4, "7", 3]
        with self.assertRaises(TypeError):
            max_integer(lst)

    def one_element_test(self):
        """Tests for list of one element"""
        lst = [2]
        self.assertEqual(max_integer(lst), 2)

    def one_negative_test(self):
        """Tests for one negative number in the list"""
        lst = [36, 72, -36, 4, 3]
        self.assertEqual(max_integer(lst), 36)

    def all_negative_test(self):
        """Tests for all negative numbers in the list"""
        lst = [-2, -31, -10, -11, -22]
        self.assertEqual(max_integer(lst), -2)

    def max_beginning_test(self):
        """Tests for max at beginning"""
        lst = [98, 19, 3, 17]
        self.assertEqual(max_integer(lst), 98)

    def max_middle_test(self):
        """Tests for max in middle"""
        lst = [33, 38, 49, 23, 40]
        self.assertEqual(max_integer(lst), 49)

    def max_end_test(self):
        """Tests for max at end"""
        lst = [59, 52, 25, 67, 90]
        self.assertEqual(max_integer(lst), 90)


if __name__ == "__main__":
    unittest.main()
