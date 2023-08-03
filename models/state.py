#!/usr/bin/python3
"""state.py
This module defines the class State.
"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """This class defines the name of the state"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state",
                              passive_deletes=True)
    else:

        @property
        def cities(self):
            """cities attribute"""

            liste = []
            objs = models.storage.all(City)

            for k, v in objs.items():
                if v.state_id == self.id:
                    liste.append(v)
            return liste
