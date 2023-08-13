#!/usr/bin/python3
"""
Unittest for file_storage.py
"""
import unittest
from os import path
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for methods in FileStorage class
    """
    def test_all(self):
        """
        Test return value of all() method
        """
        fs = FileStorage()
        objects = fs.all()
        self.assertIs(type(objects), dict)

    def test_new(self):
        """
        Test if an object was added to a dictionary 
        """
        from models.base_model import BaseModel
        bs = BaseModel()
        bs.id = "b29b5df5-72e7-43af-8b10-0db51b6d912f"
        fs = FileStorage()
        fs.new(bs)
        objects = fs.all()
        classname_id = type(bs).__name__ + "." + str(bs.id)
        self.assertIn(classname_id, objects)

    def test_save(self):
        """
        Test if dictionary of object is saved in file
        """
        fs = FileStorage()
        fs.save()
        self.assertTrue(path.isfile("file.json"))

    def test_reload(self):
        """
        Test if dictionary of objects is reloaded from file
        """
        fs = FileStorage()
        fs.reload()
        objects = fs.all()
        self.assertIs(type(objects), dict)
