#!/usr/bin/python3

"""
Unittesting for class Rectangle
"""

import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangleClass(unittest.TestCase):
    """Test class for rectangle"""

    def test5_raiseError_noheight(self):
        """Raise error no height"""
        self.assertRaises(TypeError, Rectangle, 1)

    def test6_raiseError_nowidth(self):
        """Raise error no width"""
        self.assertRaises(TypeError, Rectangle)

    def test9_check_width(self):
        """Check width"""
        r7 = Rectangle(6, 9)
        self.assertEqual(r7.width, 6)

    def test10_bad_width(self):
        """invalid width"""
        self.assertRaises(ValueError, Rectangle, -3, 8, id=10)

    def test11_width_str(self):
        """Check width as string"""
        self.assertRaises(TypeError, Rectangle, "four", 8, id=69)

    def test12_check_length(self):
        """Check valid height"""
        r8 = Rectangle(6, 9, id=11)
        self.assertEqual(r8.height, 9)

    def test13_bad_length(self):
        """Check neg height"""
        self.assertRaises(ValueError, Rectangle, 3, -7, id=11)

    def test14_height_str(self):
        """Check height as string"""
        self.assertRaises(TypeError, Rectangle, 3, "five", id=52)

    def test15_check_width_list(self):
        """Check width as list"""
        self.assertRaises(TypeError, Rectangle, [4, 7], 2, id=25)

    def test16_check_height_list(self):
        """Check height as list"""
        self.assertRaises(TypeError, Rectangle, 2, [5, 10], id=100)

    def test_check_width_TypeError_02(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(TypeError,
                               'width must be an integer',
                               Rectangle,
                               [6, 4, 9, 9], 2, 0, 0, 12)

    def test_check_width_ValueError(self):
        """Test TypeError for width in Rectangle"""
        self.assertRaisesRegex(ValueError,
                               'width must be > 0',
                               Rectangle,
                               -1, 2, 0, 0, 12)

    def test_check_height_TypeError_02(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(TypeError,
                               'height must be an integer',
                               Rectangle,
                               3, [1, 2, 3, 4], 0, 0, 12)

    def test_check_height_ValueError(self):
        """Test TypeError for height in Rectangle"""
        self.assertRaisesRegex(ValueError,
                               'height must be > 0',
                               Rectangle,
                               1, -2, 0, 0, 12)


    def test_x_TypeError_01(self):
        """TypeError for x in Rectangle but on purpose"""
        self.assertRaisesRegex(TypeError,
                               'x must be an integer',
                               Rectangle,
                               4, 2, 'string''', 0, 12)

    def test_check_x_TypeError_02(self):
        """Test TypeError for x it's a list this time"""
        self.assertRaisesRegex(TypeError,
                               'x must be an integer',
                               Rectangle,
                               4, 2, [1, 2, 3, 4], 0, 12)

    def test_check_x_ValueError(self):
        """Test ValueError for x now it's 0 muahahah"""
        self.assertRaisesRegex(ValueError,
                               'x must be >= 0',
                               Rectangle,
                               4, 2, -1, 0, 12)

    def test_check_y(self):
        """Yest y of rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 6, 4)
        self.assertEqual(r2.y, 4)

        r3 = Rectangle(5, 2, 3, 9, 12)
        self.assertEqual(r3.y, 9)

        r4 = Rectangle(5, 2, 3, 0, 12)
        self.assertEqual(r4.y, 0)

    def test_check_y_TypeError(self):
        """y be string"""
        self.assertRaisesRegex(TypeError,
                               'y must be an integer',
                               Rectangle,
                               4, 2, 0, 'string', 12)

    def test_check_y_TypeError_02(self):
        """when u can be list"""
        self.assertRaisesRegex(TypeError,
                               'y must be an integer',
                               Rectangle,
                               4, 2, 0, [1, 2, 3, 4], 12)

    def test_check_y_TypeError_(self):
        """y is 0 yes"""
        self.assertRaisesRegex(ValueError,
                               'y must be >= 0',
                               Rectangle,
                               4, 2, 0, -6, 12)

if __name__ == '__main__':
    unittest.main()
