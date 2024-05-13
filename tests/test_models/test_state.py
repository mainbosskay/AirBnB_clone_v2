#!/usr/bin/python3
"""Unittest for state.py has been established"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from os import getenv


class test_state(test_basemodel):
    """Unittest for initializing an instance of State class is defined"""

    def __init__(self, *args, **kwargs):
        """Initializing test for State class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test State 'name' attr"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.name), expctmsg)
