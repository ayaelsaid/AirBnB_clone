#!/usr/bin/python3
"""
unittests for base_model.py
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ test cases for base_model.py"""
    def get_dict_base():
        """get the dictionary"""
        my_model = BaseModel()
        input = {my_model.name: "My First Model", my_model.my_number: 89}
        output =
        {
                f"[BaseModel] ({my_model.id}) ":
                {
                    'id': my_model.id,
                    'create_at': my_model.create_at.isoformat(),
                    'updated_at': my_model.updated_at.isoformatt(),
                    'name': my_model.name,
                    'my_number': my_model.my_number
                }
        }
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
