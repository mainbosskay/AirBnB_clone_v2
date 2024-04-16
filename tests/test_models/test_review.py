#!/usr/bin/python3
"""Unittest for review.py has been established"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from os import getenv


class test_review(test_basemodel):
    """Unittest for initializing an instance of Review class is defined"""

    def __init__(self, *args, **kwargs):
        """Initializing test of the Review class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test Review 'place_id' attr"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.place_id), expctmsg)

    def test_user_id(self):
        """Test Review 'user_id' attr"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.user_id), expctmsg)

    def test_text(self):
        """Test Review 'text' attr"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.text), expctmsg)
