#!/usr/bin/python3
"""Unittest for base_model.py has been established"""
from models.base_model import BaseModel, Base
import unittest
import datetime
import json
from uuid import UUID
from os import getenv


class test_basemodel(unittest.TestCase):
    """Unittest for instantiating object of BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializing the test class for the BaseModel"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Setup environment for test class"""
        pass

    def tearDown(self):
        """Clean up environment after test class"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """Test default initialization of the BaseModel class"""
        self.assertIsInstance(self.value(), BaseModel)
        if self.value is not BaseModel:
            self.assertIsInstance(self.value(), Base)
        else:
            self.assertNotIsInstance(self.value(), Base)

    def test_kwargs(self):
        """Test BaseModel with keyword arguments"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test BaseModel with integer as keyword arguments"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test 'str' method of BaseModel for a string representation"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test BaseMode 'to_dict' dictionary representation method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)
        self.assertIsInstance(self.value().to_dict(), dict)
        self.assertIn('id', self.value().to_dict())
        self.assertIn('created_at', self.value().to_dict())
        self.assertIn('updated_at', self.value().to_dict())
        inst = self.value()
        inst.firstname = 'Daniel'
        inst.lastname = 'James'
        self.assertIn('firstname', inst.to_dict())
        self.assertIn('lastname', inst.to_dict())
        self.assertIn('firstname', self.value(firstname='Joe').to_dict())
        self.assertIn('lastname', self.value(lastname='Dan').to_dict())
        self.assertIsInstance(self.value().to_dict()['created_at'], str)
        self.assertIsInstance(self.value().to_dict()['updated_at'], str)
        currntdt = datetime.datetime.today()
        inst = self.value()
        inst.id = '24411'
        inst.created_at = inst.updated_at = currntdt
        to_dict = {
                'id': '24411',
                '__class__': inst.__class__.__name__,
                'created_at': currntdt.isoformat(),
                'updated_at': currntdt.isoformat()
        }
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertDictEqual(
                    self.value(id='ai12', age=20).to_dict(),
                    {
                        '__class__': inst.__class__.__name__,
                        'id': 'ai12',
                        'age': 20
                    }
            )
        dictinst = self.value()
        self.assertIn('__class__', self.value().to_dict())
        self.assertNotIn('__class__', self.value().__dict__)
        self.assertNotEqual(dictinst.to_dict(), dictinst.__dict__)
        self.assertNotEqual(
                dictinst.to_dict()['__class__'],
                dictinst.__class__
        )
        with self.assertRaises(TypeError):
            self.value().to_dict(None)
        with self.assertRaises(TypeError):
            self.value().to_dict(self.value())
        with self.assertRaises(TypeError):
            self.value().to_dict(32)
        self.assertNotIn('_sa_instance_state', n)

    def test_kwargs_none(self):
        """Test BaseModel with no key and value passed as keyword args"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test BaseModel with single argument passed as keyword argument"""
        n = {'name': 'test'}
        new = self.value(**n)
        self.assertEqual(new.name, n['name'])

    def test_id(self):
        """Test 'id' attr of the BaseModel"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test 'created_at' attr of the BaseModel"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test 'updated_at' attr of the BaseModel"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_delete(self):
        """Test BaseModel 'delete' method"""
        from models import storage
        i = self.value()
        i.save()
        self.assertTrue(i in storage.all().values())
        i.delete()
        self.assertFalse(i in storage.all().values())
