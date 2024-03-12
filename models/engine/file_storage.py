#!/usr/bin/python3

import os
import json
from models.base_model import base_model


class FileStorage:
    """ define class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        obj__cls__name = obj.__class__.__name__
        key1 = "{}.{}".format(obj__cls__name, obj.id)
        FileStorage.__objects[key1] = obj

    def save(self):
        all__objs = FileStorage.__objects
        dict_obj = {}
        for obj in all__objs.keys():
            dict_obj[obj] = all__objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(dict_obj, file)
