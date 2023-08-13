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
        obj.id = "b29b5df5-72e7-43af-8b10-0db51b6d912f"
        fs = FileStorage()
        fs.new(obj)
        objects = fs.all()
        classname_id = type(obj).__name__ + "." + str(obj.id)
        self.assertIn(classname_id, objects)
