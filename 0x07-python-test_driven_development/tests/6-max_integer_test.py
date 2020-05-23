#!/usr/bin/python3
"""
unitest
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):
    """
    test

    Arguments:
        unittest {[unitest]} -- [description]
    """
    def test_start(self):
        """
        test
        """
        self.assertEqual(max_integer([7, 5, 6, 7]), 7)

    def test_mid(self):
        """
        3 matrix
        """
        self.assertEqual(max_integer([5, 6, 5]), 6)

    def test_neg(self):
        """
        negative num
        """
        self.assertEqual(max_integer([5, -6, 7]), 7)

    def test_neg_all(self):
        """
        only negatives
        """
        self.assertEqual(max_integer([-5, -6, -7]), -5)

    def test_normal(self):
        """
        normal
        """
        self.assertEqual(max_integer([5, 6, 7]), 7)

    def test_len(self):
        """
        list copy
        """
        list = [5, 6, 7]
        copy = list.copy()
        self.assertEqual(max_integer([5, 6, 7]), 7)
        self.assertEqual(len(list), len(copy))
        for a in range(len(list)):
            self.assertEqual(list[a], copy[a])

    def test_duplicate(self):
        """
        descr
        """
        self.assertEqual(max_integer([5, 6, 7, 7]), 7)

    def test_none(self):
        """
        none
        """
        self.assertEqual(max_integer([]), None)

    def test_single(self):
        """
        by 1
        """
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
