#!/usr/bin/python3.8
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from os import getenv

storageType = getenv("HBNB_TYPE_STORAGE")


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(new.name, None)
