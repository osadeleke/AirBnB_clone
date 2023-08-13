#!/usr/bin/python3
"""
Unittests for review.py
"""
import unittest
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """
    Test cases for Review class
    """
    def test_review_obj(self):
        """
        Test if Review object can be created
        """
        from models.review import Review
        obj = Review()
        obj.id = "b29b5df5-72e7-43af-8b10-0db51b6d912f"
        fs = FileStorage()
        fs.new(obj)
        objects = fs.all()
        classname_id = type(obj).__name__ + "." + str(obj.id)
        self.assertIn(classname_id, objects)
