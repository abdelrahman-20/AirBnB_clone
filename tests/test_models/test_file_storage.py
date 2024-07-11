#!/usr/bin/python3
"""This is The Test Module For FileStorage Class."""

import sys
import unittest
from datetime import datetime

sys.path.append("../../models/engine")
file_storage = __import__("file_storage")
FileStorage = file_storage.FileStorage


class TestFileStorage(unittest.TestCase):
    """Test For FileStorage"""

    def setUp(self):
        """creates a test object for other tests"""
        self.test_object = FileStorage()


if __name__ == "__main__":
    unittest.main()
