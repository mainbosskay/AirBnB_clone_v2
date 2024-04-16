#!/usr/bin/python3
"""Unittest for place.py has been established"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from os import getenv


class test_Place(test_basemodel):
    """Unittest for initializing an instance of Place class is defined"""

    def __init__(self, *args, **kwargs):
        """Initializing the Place test class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test 'city_id' attr of the Place"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.city_id), expctmsg)

    def test_user_id(self):
        """Test 'user_id' attr of the Place"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.user_id), expctmsg)

    def test_name(self):
        """Test 'name' attr of the Place"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.name), expctmsg)

    def test_description(self):
        """Test 'description' attr of the Place"""
        new = self.value()
        expctmsg = str if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.description), expctmsg)

    def test_number_rooms(self):
        """Test 'number_rooms' attr of the Place"""
        new = self.value()
        expctmsg = int if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.number_rooms), expctmsg)

    def test_number_bathrooms(self):
        """Test 'number_bathrooms' attr of the Place"""
        new = self.value()
        expctmsg = int if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.number_bathrooms), expctmsg)

    def test_max_guest(self):
        """Test 'max_guest' attr of the Place"""
        new = self.value()
        expctmsg = int if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.max_guest), expctmsg)

    def test_price_by_night(self):
        """Test 'price_by_night' attr of the Place"""
        new = self.value()
        expctmsg = int if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.price_by_night), expctmsg)

    def test_latitude(self):
        """Test 'latitude' attr of the Place"""
        new = self.value()
        expctmsg = float if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.latitude), expctmsg)

    def test_longitude(self):
        """Test 'lonitude' attr of the Place"""
        new = self.value()
        expctmsg = float if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.latitude), expctmsg)

    def test_amenity_ids(self):
        """Test 'amenity_ids' attr of the Place"""
        new = self.value()
        expctmsg = list if getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.amenity_ids), expctmsg)
