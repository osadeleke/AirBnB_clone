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
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.state_id, "")
