#!/usr/bin/python3
"""Unittest for amenity.py has been established"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from os import getenv


class test_Amenity(test_basemodel):
    """Unittest for instantiating an object of Amenity class is defined"""

    def __init__(self, *args, **kwargs):
        """Initializing test for Amenity class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test Amenity 'name' attr"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.name), expctmsg)
