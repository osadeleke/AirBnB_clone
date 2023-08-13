#!/usr/bin/python3
"""
Unittests for state.py
"""
import unittest
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """
    Test cases for State class
    """
    def test_state_obj(self):
        """
        Test if State object can be created
        """
        from models.state import State
        obj = State()
        obj.id = "b29b5df5-72e7-43af-8b10-0db51b6d912f"
        fs = FileStorage()
        fs.new(obj)
        objects = fs.all()
        classname_id = type(obj).__name__ + "." + str(obj.id)
        self.assertIn(classname_id, objects)
