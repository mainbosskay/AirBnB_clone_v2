#!/usr/bin/python3
"""Unittest for user.py has been established"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from os import getenv


class test_User(test_basemodel):
    """Unittest for initializing an instance of User class is defined"""

    def __init__(self, *args, **kwargs):
        """Initializing User class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test 'first_name' attr of the User"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.first_name), expctmsg)

    def test_last_name(self):
        """Test 'last_name' attr of the User"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.last_name), expctmsg)

    def test_email(self):
        """Test 'email' attr of the User"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.email), expctmsg)

    def test_password(self):
        """Test 'password' attr of the User"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.password), expctmsg)
