"""Base Model Class Module"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """The BaseModel Class For AirBnB Project."""

    def __init__(self):
        """Initialize Class Object Attributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """Update The Value of Object Attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """A Method To Return A Dictionary of Object Attributes."""

        object_dict = self.__dict__.copy()
        for k, v in self.__dict__.items():
            object_dict[k] = v

        object_dict["__class__"] = self.__class__.__name__
        object_dict["created_at"] = self.created_at.isoformat()
        object_dict["updated_at"] = self.created_at.isoformat()

    def __str__(self):
        """Return A Formatted Representation of The Class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
