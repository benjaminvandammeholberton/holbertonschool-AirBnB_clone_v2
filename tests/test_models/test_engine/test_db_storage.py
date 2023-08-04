#!/usr/bin/python3
import pycodestyle
import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """Test class for db storage"""

    def test_doc(self):
        """Tests the documentation"""

        self.assertGreater(len(console.__doc__), 0)

        self.assertGreater(len(HBNBCommand.__doc__), 0)

        self.assertGreater(len(HBNBCommand.do_all.__doc__), 0)

        self.assertGreater(len(HBNBCommand.do_create.__doc__), 0)

        self.assertGreater(len(HBNBCommand.do_destroy.__doc__), 0)

        self.assertGreater(len(HBNBCommand.do_quit.__doc__), 0)

        self.assertGreater(len(HBNBCommand.do_EOF.__doc__), 0)

        self.assertGreater(len(HBNBCommand.do_count.__doc__), 0)

        self.assertGreater(len(HBNBCommand.do_destroy.__doc__), 0)

        self.assertGreater(len(HBNBCommand.do_update.__doc__), 0)

        self.assertGreater(len(HBNBCommand.emptyline.__doc__), 0)

        self.assertGreater(len(HBNBCommand.default.__doc__), 0)

    def test_pep8_console(self):
        """pep8 test"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

