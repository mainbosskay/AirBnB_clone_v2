#!/usr/bin/python3
"""Unittest for City.py has been established"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from os import getenv


class test_City(test_basemodel):
    """Unittest for initializing an instance of City class is defined"""

    def __init__(self, *args, **kwargs):
        """Initializing test class of city"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test City 'state_id' attr"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.state_id), expctmsg)

    def test_name(self):
        """Test City 'name' attr"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.name), expctmsg)
