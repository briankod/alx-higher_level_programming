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

if __name__ == "__main__":
    unittest.main()
