#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(
                String(128),
                nullable=False
        )
        cities = relationship(
                'City',
                cascade='all, delete, delete-orphan',
                backref='state'
        )
    else:
        name = ""

        @property
        def cities(self):
            """ Returning list of City instances with state_id """
            from models import storage
            cits_in_stts = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    cits_in_stts.append(city)
            return cits_in_stts
