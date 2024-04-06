#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ define class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        obj__cls__name = obj.__class__.__name__
        key1 = "{}.{}".format(obj__cls__name, obj.id)
        FileStorage.__objects[key1] = obj

    def all(self):
        return FileStorage.__objects

    def save(self):
        all__objs = FileStorage.__objects
        dict_obj = {}
        for obj in all__objs.keys():
            dict_obj[obj] = all__objs[obj].to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(dict_obj, file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    dict_obj = json.load(file)
                    for key1, value in dict_obj.items():
                        class__name, obj_id =key1.split('.')
                        cls =  eval(class__name)
                        instance = cls(**values)
                        FileStorage.__objects[key1] = instance
                except Exception:
                    pass
