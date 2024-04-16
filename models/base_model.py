#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(
            String(60),
            nullable=False,
            primary_key=True,
            unique=True
    )
    created_at = Column(
            DATETIME,
            nullable=False,
            default=datetime.utcnow()
    )
    updated_at = Column(
            DATETIME,
            nullable=False,
            default=datetime.utcnow()
    )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key != '__class__':
                    setattr(self, key, kwargs[key])
            if getenv('HBNB_TYPE_STORAGE') == 'db':
                if kwargs.get('id') is None:
                    setattr(self, 'id', str(uuid.uuid4()))
                if kwargs.get('created_at') is None:
                    setattr(self, 'created_at', datetime.now())
                if kwargs.get('updated_at') is None:
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictinst = self.__dict__.copy()
        dictinst['__class__'] = self.__class__.__name__
        for key in dictinst:
            if type(dictinst[key]) is datetime:
                dictinst[key] = dictinst[key].isoformat()
        if '_sa_instance_state' in dictinst.keys():
            del(dictinst['_sa_instance_state'])
        return dictinst

    def delete(self):
        """Deleting current instance from the storage"""
        from models import storage
        storage.delete(self)
