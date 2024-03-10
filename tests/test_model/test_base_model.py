#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_int(self):
        my_model = BaseModel()
        
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        my_model = BaseModel()
        
        init_updated_at = my_model.updated_at
        curr_updated_at = my_model.save()
        self.assertNotEqual(init_updated_at, curr_updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model_dct = my_model.to_dict()
        self.assertIsInstance(my_model_dct, dict)
        
        self.assertEqual(my_model_dct["__class__"], 'BaseModel')
        