#!/usr/bin/python3
"""
File to manage the database
This script defines the DBStorage engine class.
"""
import os
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """
    Represents a database storage engine.
    Attributes:
        __engine (sqlalchemy.Engine): The SQLAlchemy engine.
        __session (sqlalchemy.Session): The SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Create a new instance of DBStorage"""
        # MySQL user, password, host, and database from environment variables
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
        db_name = os.environ.get('HBNB_MYSQL_DB')

        # Construct the database URI
        db_uri = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(user, pwd, host, db_name)

        self.__engine = create_engine(db_uri, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """
        Queries the current database session
        for all objects of the given class.
        """
        result = {}
        classes = {
            'State': State, 'City': City, 'User': User,
            'Place': Place, 'Review': Review, 'Amenity': Amenity
        }

        # Import storage here to avoid circular import
        from models import storage

        if cls is None:
            for c in classes.values():
                query_result = self.__session.query(c).all()
                for obj in query_result:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result[key] = obj
        else:
            query_result = self.__session.query(classes[cls]).all()
            for obj in query_result:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj

        return result

    def new(self, obj):
        """
        Adds obj to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from the current database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and initializes a new session.
        """
        self.__session.close()
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """
        Closes the working SQLAlchemy session.
        """
        self.__session.remove()
