#!/usr/bin/python3

"""Test class base"""

import unittest
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


class TestBase(unittest.TestCase):
    """Test base class unittesting"""

    def test_increment(self):
        """test increment"""
        Base._Base__nb_objects = 0
        b0 = Base()
        self.assertIs(b0.id, 1)

        b1 = Base()
        self.assertIs(b1.id, 2)

        b2 = Base()
        self.assertIs(b2.id, 3)

    def test_input(self):
        """test input types"""
        Base._Base__nb_objects = 0

        b_norm = Base()
        self.assertEqual(b_norm.id, 1)

        b_46 = Base(46)
        self.assertEqual(b_46.id, 46)

        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_neg_input(self):
        """neg input"""
        Base._Base__nb_objects = 0

        b_norm = Base()
        self.assertEqual(b_norm.id, 1)

        b_neg2 = Base(-2)
        self.assertEqual(b_neg2.id, -2)

        b3 = Base()
        self.assertEqual(b3.id, 2)
    def test_1(self):
        """tests for task 1"""
        base0 = Base()
        self.assertEqual(base0.id, 1)
        self.assertEqual(type(base0), Base)

        Base._Base__nb_objects = 3
        base1 = Base()
        self.assertEqual(base1.id, 4)
        self.assertEqual(isinstance(base1, Base), True)

        Base._Base__nb_objects = -2
        base2 = Base()
        self.assertEqual(base2.id, -1)

    def test_id(self):
        """test id"""
        test = Base()
        self.assertEqual(type(test.id), int)

    def test_to_json_string(self):
        """test json to string"""
        r = Rectangle(10, 5, 5, 5)
        testd = r.to_dictionary()
        jdict = Base.to_json_string([testd])
        self.assertEqual(type(jdict), str)

    def test_to_json_string_none(self):
        """test json to string none"""
        jsonstr = None
        Base.to_json_string(jsonstr)
        self.assertEqual(jsonstr, None)

    def test_save_to_file_null(self):
        """test save to file null"""
        lo = None
        Base.save_to_file(lo)
        self.assertEqual(os.path.exists('Base.json'), True)

    def test_save_to_file_data_type(self):
        """test save to file data type"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = file.read()
        self.assertEqual(type(data), str)

    def test_save_to_file_empty_contents(self):
        """test save to file empty contents"""
        lo = None
        Base.save_to_file(lo)
        with open("Base.json", mode='r') as f:
            data = f.read()
        self.assertEqual(data, '[]')

    def test_from_json_string_none(self):
        """test from json string none"""
        lo = None
        jsonstr = Base.from_json_string(lo)
        self.assertEqual(jsonstr, None or [])

    def test_from_json_string_data_type(self):
        """test json to string data type"""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_create_instance(self):
        """test create instance"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(isinstance(r2, Base), True)

    def test_create_class_name(self):
        """test create class name"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1 is r2 and r1 == r2, False)

if __name__ == '__main__':
    unittest.main()
