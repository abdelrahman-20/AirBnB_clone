#!/usr/bin/python3
"""The File Storage Model of The Project"""

import os
import json
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """A Class To Handle Storing Data."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Function To Return Objects Dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Set The Object Key and Value in __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects To The JSON File"""
        with open(FileStorage.__file_path, "w") as fp:
            if FileStorage.__objects.items():
                json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, fp)
            else:
                json.dump({}, fp)

    def reload(self):
        """Deserializes __objects From The JSON File"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as fp:
            FileStorage.__objects = json.load(fp)

    def my_class_list(self):
        classes = {
            "BaseModel": BaseModel,
        }
        return classes

    def my_class_attributes(self):
        return {
            "BaseModel": {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime
            }
        }
