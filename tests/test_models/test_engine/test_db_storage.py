#!/usr/bin/python3
""" """
import pycodestyle
import unittest
from models.engine.db_storage import DBStorage


class test_db_storage(unittest.TestCase):
    """Test class for db storage"""

    def test_pep8_DBStorage(self):
        """pep8 test"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_documentation_module(self):
        """Tests the the documentation of the module"""
        self.assertGreater(len(DBStorage.__doc__), 0)

    def test_documentation_class(self):
        """Tests the the documentation of the class"""
        self.assertGreater(len(DBStorage.__doc__), 0)

    def test_documentation_init(self):
        """Tests the the documentation of init"""
        self.assertGreater(len(DBStorage.__init__.__doc__), 0)

    def test_documentation_all(self):
        """Tests the the documentation of all"""
        self.assertGreater(len(DBStorage.all.__doc__), 0)

    def test_documentation_new(self):
        """Tests the the documentation of new"""
        self.assertGreater(len(DBStorage.new.__doc__), 0)

    def test_documentation_save(self):
        """Tests the the documentation of save"""
        self.assertGreater(len(DBStorage.save.__doc__), 0)

    def test_documentation_delete(self):
        """Tests the the documentation of delete"""
        self.assertGreater(len(DBStorage.delete.__doc__), 0)

    def test_documentation_reload(self):
        """Tests the the documentation of reload"""
        self.assertGreater(len(DBStorage.reload.__doc__), 0)
