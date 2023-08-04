#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        initial_count = len(storage.all())  # Nombre initial d'objets dans le stockage
        new = BaseModel()
        new_key = new.__class__.__name__ + "." + new.id
        objects = storage.all()
        self.assertTrue(new_key in objects)
        self.assertEqual(len(objects), initial_count + 1)  # Vérifie si le nombre d'objets a augmenté

    def test_save(self):
        """ Test if the file is correctly saved """
        new = BaseModel()
        new.save()
        key = new.__class__.__name__ + "." + new.id
        objects = storage.all()
        self.assertTrue(key in objects)

    def test_reload(self):
        """ Test if the file is correctly loaded """
        new = BaseModel()
        new_key = new.__class__.__name__ + "." + new.id
        new.save()
        storage.reload()  # Reload data from file
        objects = storage.all()
        self.assertTrue(new_key in objects)

    def test_delete(self):
        """ Test if object is correctly deleted """
        new = BaseModel()
        new.save()
        key = new.__class__.__name__ + "." + new.id
        objects = storage.all()
        self.assertTrue(key in objects)
        storage.delete(new)  # Delete the object
        objects = storage.all()
        self.assertFalse(key in objects)


if __name__ == '__main__':
    unittest.main()
