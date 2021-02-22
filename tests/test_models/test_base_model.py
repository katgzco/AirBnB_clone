#!/usr/bin/python3
""" Module Unittest for BaseModel """


from unittest import TestCase
import pep8
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(TestCase):
    """ test class BaseModel """

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8.
        """
        style = pep8.StyleGuide()
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    @classmethod
    def setUpClass(cls):
        """Define all attributes for test the class methods
        """
        cls.base1 = BaseModel()
        cls.base2 = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """After run the Test clase remove the instance create
        for the test
        """
        del cls.base1
        del cls.base2

    def setUp(self):
        """Clean code after each test
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        FileStorage.FileStorage__objects = {}

    def test_docstring(self):
        """ Test doc strings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_inicialization_args(self):
        """Test the inicialization of the class with args
        """
        self.assertIsInstance(self.base1, BaseModel)
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertTrue(type(self.base1.created_at) == datetime)
        self.assertTrue(type(self.base1.updated_at) == datetime)
        self.assertNotEqual(self.base1.id, self.base2.id)

    def test_save(self):
        """Test Base Model save method
        """
        old_update = self.base1.updated_at
        self.base1.save()
        self.assertFalse(old_update == self.base1.updated_at)

    def test_to_dict(self):
        self.base1.name = "Lupe"
        self.assertIn("id", self.base1.to_dict())
        self.assertIn("created_at", self.base1.to_dict())
        self.assertIn("updated_at", self.base1.to_dict())
        self.assertIn("__class__", self.base1.to_dict())
        # Check if set a new attribute in the dictionary
        self.assertIn("name", self.base1.to_dict())

    def test_str(self):
        """Test BaseModel str method
        """
        self.assertTrue(type(self.base2.__str__()) == str)


if __name__ == "__main__":
    unittest.main()
