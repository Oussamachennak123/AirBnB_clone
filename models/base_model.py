#!/usr/bin/python3
import sys
import uuid
from datetime import datetime
import models
""" define class BaseModel"""


class BaseModel:
    def __init__(self, *arg, **kwargs):
        tim_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key1, value in kwargs.items():
                if key1 == "__class__":
                    continue
                elif key1 == "created_at" or key1 == "updated_at":
                    setattr(self, key1, datetime.strptime(value, tim_format))
                else:
                    setattr(self, key1, value)
        else:
            self.id = str(uuid.uuid4())

            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        
        models.Storage.new(self)

    def save(self):
        """A method to save attributes
        """
        self.updated_at = datetime.utcnow()
        models.Storage.save()

    def to_dict(self):
        """the key-paired values to dictionary
        Returns:
            dict: return dictionary
        """
        inst__dict = self.__dict__.copy()
        inst__dict["__class"] = self.__class__.__name__
        inst__dict["created_at"] = self.created_at.isoformat()
        inst__dict["updated_at"] = self.updated_at.isoformat()

        return inst__dict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                       my_model_json[key]))
