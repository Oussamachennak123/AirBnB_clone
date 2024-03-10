#!/usr/bin/python3
import sys
import uuid
from datetime import datetime
""" define class BaseModel"""


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """A method to save attributes
        """
        self.updated_at = datetime.now

    def to_dict(self):
        """the key-paired values to dictionary
        Returns:
            dict: return dictionary
        """
        key11_dict = {'__class__': self.__class__.__name__}
        key11_dict.update({aa: bb.isoformat()
                        if isinstance(bb, datetime)
                        else bb for aa, bb in self.__dict__.items()})
        return key11_dict


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
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
