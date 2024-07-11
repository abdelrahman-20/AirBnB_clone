#!/usr/bin/python3
"""The Base Model of The Project"""

import uuid
from datetime import datetime


# from models import storage


class BaseModel:
    """The BaseModel Class For AirBnB Project."""

    def __init__(self, *args, **kwargs):
        """The Constructor Function of The Class."""
        if kwargs:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)
        del kwargs["__class__"]

    def save(self):
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        for key, val in self.__dict__.items():
            obj_dict[key] = val

        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
