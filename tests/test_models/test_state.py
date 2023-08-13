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
        self.assertEqual(obj.name, "")
