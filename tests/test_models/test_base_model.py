#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):

    def setUp(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        i = BaseModel()
        self.assertIsInstance(i, BaseModel)

    def test_kwargs(self):
        """ """
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """ """
        i = BaseModel()
        self.assertEqual(str(i), '[BaseModel] ({}) {}'.format(i.id, i.__dict__))

    def test_todict(self):
        """ """
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_id(self):
        """ """
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime)

    def test_updated_at(self):
        """ """
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = BaseModel(**n)


if __name__ == '__main__':
    unittest.main()
