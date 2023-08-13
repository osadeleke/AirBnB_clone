#!/usr/bin/python3
"""
Unittests for amenity.py
"""
import unittest
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class
    """
    def test_amenity_obj(self):
        """
        Test if Amenity object can be created
        """
        from models.amenity import Amenity
        obj = Amenity()
        self.assertEqual(obj.name, "")
