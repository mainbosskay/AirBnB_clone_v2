#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column(
                'place_id',
                String(60),
                ForeignKey('places.id'),
                primary_key=True,
                nullable=False
            ),
            Column(
                'amenity_id',
                String(60),
                ForeignKey('amenities.id'),
                primary_key=True,
                nullable=False
            )
    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(
                String(60),
                ForeignKey('cities.id'),
                nullable=False
        )
        user_id = Column(
                String(60),
                ForeignKey('users.id'),
                nullable=False
        )
        name = Column(
                String(128),
                nullable=False
        )
        description = Column(
                String(1024),
                nullable=True
        )
        number_rooms = Column(
                Integer,
                nullable=False,
                default=0
        )
        number_bathrooms = Column(
                Integer,
                nullable=False,
                default=0
        )
        max_guest = Column(
                Integer,
                nullable=False,
                default=0
        )
        price_by_night = Column(
                Integer,
                nullable=False,
                default=0
        )
        latitude = Column(
                Float,
                nullable=True
        )
        longitude = Column(
                Float,
                nullable=True
        )
        reviews = relationship(
                'Review',
                cascade='all, delete, delete-orphan',
                backref='place'
        )
        amenities = relationship(
                'Amenity',
                secondary=place_amenity,
                viewonly=False,
                backref='place_amenities'
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Returning list of Review instances with place_id """
            from models import storage
            revwall = storage.all(Review)
            revslst = []
            for revw in revwall.values():
                if revw.place_id == self.id:
                    revwlst.append(revw)
            return revwlst

        @property
        def amenities(self):
            """ Returning list of Amenity instances based on amenity_ids """
            from models import storage
            amntyall = storage.all(Amenity)
            amntylst = []
            for amnty in amntyall.values():
                if amnty.id in self.amenity_ids:
                    amntylst.append(amnty)
            return amntylst

        @amenities.setter
        def amenities(self, amnty):
            """ Adding Amenity.id to the attr amenity_ids """
            if amnty is not None:
                if isinstance(amnty, Amenity):
                    if amnty.id not in self.amenity_ids:
                        self.amenity_ids.append(amnty.id)
