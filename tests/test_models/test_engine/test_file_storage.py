#!/usr/bin/python3
""" Module Unittest for City """

from unittest import TestCase
import pep8
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


class TestFileStorage(TestCase):
    """ test class City """

    models = {"BaseModel": BaseModel, "User": User,
              "City": City, "Amenity": Amenity,
              "Place": Place, "Review": Review,
              "State": State}

    def setUp(self):
        """Clean code after each test.
        """
        if os.path.isfile("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8.
        """
        style = pep8.StyleGuide()
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_docstring(self):
        """ Test doc strings
        """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all(self):
        """Test all method
        """
        self.assertIsInstance(storage.all(), dict)
        self.assertTrue(storage.all() is storage._FileStorage__objects)

    def test_new(self):
        """Test new method
        """
        for key, value in TestFileStorage.models.items():
            instance = value()
            storage.new(instance)
            key_obj = "{}.{}".format(type(instance).__name__, instance.id)
            self.assertTrue(key_obj in storage.all())
            self.assertTrue(storage.all()[key_obj], instance)

    def test_save(self):
        """Test for save method
        """
        for key, value in TestFileStorage.models.items():
            instance = value()
            storage.new(instance)
            storage.save()
        with open("file.json") as file:
            self.assertIsInstance(json.load(file), dict)

    def test_reload(self):
        """Test for reload method
        """
        for key, value in TestFileStorage.models.items():
            instance = value()
            tmp_id = instance.id
            storage.new(instance)
            storage.reload()
            key_obj = "{}.{}".format(key, tmp_id)
            tmp_dic = storage.all()
            self.assertTrue(key_obj in tmp_dic)


if __name__ == "__main__":
    unittest.main()
