#!/usr/bin/python3
""" Module Unittest for Amenity """

import pep8
from unittest import TestCase
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(TestCase):
    """ test class Amenity """
    @classmethod
    def setUpClass(cls):
        """Define all attributes for test the class methods
        """
        cls.amenity1 = Amenity()

    @classmethod
    def tearDownClass(cls):
        """After run the Test clase remove the instance create
        for the test
        """
        del cls.amenity1

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8.
        """
        style = pep8.StyleGuide()
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_docstring(self):
        """ Test doc strings
        """
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def test_inherits_BaseModel(self):
        """Test if the innstance is a subclas of BaseModel
        """
        self.assertTrue(issubclass(type(self.amenity1), BaseModel))

    def test_inicialization(self):
        """Test initizalition of the instance
        """
        self.assertTrue(hasattr(self.amenity1, "name"))
        self.assertIsInstance(self.amenity1.name, str)
        self.assertTrue(self.amenity1.name == "")


if __name__ == "__main__":
    unittest.main()
