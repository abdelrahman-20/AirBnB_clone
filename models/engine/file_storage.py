#!/usr/bin/python3
"""The File Storage Model of The Project"""

import os
import json


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
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, fp)

    def reload(self):
        """Deserializes __objects From The JSON File"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as fp:
                json_object = json.load(fp)
                json_object = {k: self.classes()[v["__class__"]](**v)
                               for k, v in json_object.items()}
        self.__objects = json_object
