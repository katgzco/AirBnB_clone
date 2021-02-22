#!/usr/bin/python3
""" Module Unittest for City """

import pep8
from unittest import TestCase
from models.base_model import BaseModel
from models.city import City


class TestCity(TestCase):
    """ test class City """
    @classmethod
    def setUpClass(cls):
        """Define all attributes for test the class methods
        """
        cls.city1 = City()

    @classmethod
    def tearDownClass(cls):
        """After run the Test clase remove the instance create
        for the test
        """
        del cls.city1

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8.
        """
        style = pep8.StyleGuide()
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_docstring(self):
        """ Test doc strings
        """
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_inherits_BaseModel(self):
        """Test if the innstance is a subclas of BaseModel
        """
        self.assertTrue(issubclass(type(self.city1), BaseModel))

    def test_inicialization(self):
        """Test initizalition of the instance
        """
        self.assertTrue(hasattr(self.city1, "state_id"))
        self.assertIsInstance(self.city1.state_id, str)
        self.assertTrue(self.city1.state_id == "")
        self.assertTrue(hasattr(self.city1, "name"))
        self.assertIsInstance(self.city1.name, str)
        self.assertTrue(self.city1.name == "")


if __name__ == "__main__":
    unittest.main()
