#!/usr/bin/python3
"""
Unittests for place.py
"""
import unittest
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class
    """
    def test_place_obj(self):
        """
        Test if Place object can be created
        """
        from models.place import Place
        obj = Place()
        obj.id = "b29b5df5-72e7-43af-8b10-0db51b6d912f"
        fs = FileStorage()
        fs.new(obj)
        objects = fs.all()
        classname_id = type(obj).__name__ + "." + str(obj.id)
        self.assertIn(classname_id, objects)
