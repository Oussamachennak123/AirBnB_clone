#!/usr/bin/python3
import sys
import uuid
import models
from datetime import datetime


""" define class BaseModel"""
class BaseModel:
    def __init__(self, *_args, **kwargs):
        if kwargs:
            for key1, value1 in kwargs.items():
                if key1 == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        value1, "%Y-%m-%dT%H:%M:%S.%f")
                elif key1 == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        value1, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key1] = value1
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """A method to save attributes
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """the key-paired values to dictionary
        Returns:
            dict: return dictionary
        """
        key11_dict = {'__class__': self.__class__.__name__} # Iterates through all key-value pairs in the __dict__ attribute of the object (self)
        key11_dict.update({aa: bb.isoformat() # __dict__ is a special attribute that stores the object's instance variables
                        if isinstance(bb, datetime)
                        else bb for aa, bb in self.__dict__.items()})
        return key11_dict
