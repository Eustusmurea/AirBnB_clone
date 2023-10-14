#!/usr/bin/python3
"""Defines the BaseModel class, which serves as the foundation for other classes in the HBnB project."""

from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """Represents the BaseModel of the HBnB project.
    
    Attributes:
        id (str): A unique identifier for each instance.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.
        
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes for the instance.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime and save the instance."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.
        
        Returns:
            dict: A dictionary containing the instance's attributes and class name.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = type(self).__name__
        return rdict

    def __str__(self):
        """Return a human-readable string representation of the BaseModel instance."""
        clname = type(self).__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
