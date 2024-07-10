#!/usr/bin/python3
"""This is The Test Module For BaseModel Class."""

import sys
import unittest
from datetime import datetime
# from models.base_model import BaseModel

sys.path.append("../../models")
base_model = __import__("base_model")
BaseModel = base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Test For BaseModel"""

    def setUp(self):
        """creates a test object for other tests"""
        self.test_object = BaseModel()

    def test_save(self):
        self.assertIsInstance(self.test_object.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
