#!/usr/bin/python3
""" Module Unittest for City """

import pep8
from unittest import TestCase
from models.base_model import BaseModel
from models.user import User


class TestUser(TestCase):
    """ test class City """
    @classmethod
    def setUpClass(cls):
        """Define all attributes for test the class methods
        """
        cls.user = User()

    @classmethod
    def tearDownClass(cls):
        """After run the Test clase remove the instance create
        for the test
        """
        del cls.user

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8.
        """
        style = pep8.StyleGuide()
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_docstring(self):
        """ Test doc strings
        """
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def test_inherits_BaseModel(self):
        """Test if the innstance is a subclas of BaseModel
        """
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_inicialization(self):
        """Test initizalition of the instance
        """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertIsInstance(self.user.email, str)
        self.assertTrue(self.user.email == "")
        self.assertTrue(hasattr(self.user, "password"))
        self.assertIsInstance(self.user.password, str)
        self.assertTrue(self.user.password == "")
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertIsInstance(self.user.first_name, str)
        self.assertTrue(self.user.first_name == "")
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertIsInstance(self.user.last_name, str)
        self.assertTrue(self.user.last_name == "")
