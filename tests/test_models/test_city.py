#!/usr/bin/python3
"""
Unittests for city.py
"""
import unittest
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """
    Test cases for City class
    """
    def test_city_obj(self):
        """
        Test if City object can be created
        """
        from models.city import City
        obj = City()
        obj.id = "b29b5df5-72e7-43af-8b10-0db51b6d912f"
        fs = FileStorage()
        fs.new(obj)
        objects = fs.all()
        classname_id = type(obj).__name__ + "." + str(obj.id)
        self.assertIn(classname_id, objects)
