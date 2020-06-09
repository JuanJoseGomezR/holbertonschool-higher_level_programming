#!/usr/bin/python3

"""
Unittesting for class square
"""

import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


class TestSquareClass(unittest.TestCase):
    """
    class testing for valid/invalid outputs
    """
    def test1_inputs(self):
        """square valid input"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test2_neg(self):
        """square negative input"""
        self.assertRaises(ValueError, Square, -4)

    def test3_str(self):
        """square string input"""
        self.assertRaises(TypeError, Square, "notnumber")

    def test4_list(self):
        """square list input"""
        self.assertRaises(TypeError, Square, [69, 619])

    def test6_updates(self):
        """check if updates args"""
        s3 = Square(3)
        s3.update(69)
        self.assertEqual(s3.id, 69)

    def test7_updates(self):
        """check if updates kwargs"""
        s4 = Square(size=5)
        s4.update(size=551)
        self.assertEqual(s4.size, 551)

if __name__ == '__main__':
    unittest.main()
