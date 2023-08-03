#!/usr/bin/python3
"""

"""
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {
    'BaseModel': BaseModel, 'User': User, 'Place': Place,
    'State': State, 'City': City, 'Amenity': Amenity,
    'Review': Review
}


class DBStorage:
    """

    """
    __engine = None
    __session = None

    def __init__(self):
        """

        """
        self.__engine = create_engine(
            f"mysql+mysqldb://{os.environ.get('HBNB_MYSQL_USER')}:{os.environ.get('HBNB_MYSQL_PWD')}@{os.environ.get('HBNB_MYSQL_HOST')}/{os.environ.get('HBNB_MYSQL_DB')}", pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """

        """
        if cls is None:
            all_objects = []
            for k, v in classes.items:
                all_objects.append(session.query(v).all())

        else:
            all_objects = session.query(cls).all()

        dico = {}
        for item in all_objects:
            k = type(item).__name__ + '.' + item.id
            dico[k] = item

        return dico

    def new(self, obj):
        """

        """
        self.__session.add(obj)

    def save(self):
        """

        """
        self.__session.commit()

    def delete(self, obj=None):
        """

        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """

        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))()

    def close(self):
        """

        """
        self.__session.close()
