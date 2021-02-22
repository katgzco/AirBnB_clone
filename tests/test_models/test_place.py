#!/usr/bin/python3
""" Module Unittest for Place """

import pep8
from unittest import TestCase
from models.base_model import BaseModel
from models.place import Place


class TestPlace(TestCase):
    """ test class City """
    @classmethod
    def setUpClass(cls):
        """Define all attributes for test the class methods
        """
        cls.place1 = Place()

    @classmethod
    def tearDownClass(cls):
        """After run the Test clase remove the instance create
        for the test
        """
        del cls.place1

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8.
        """
        style = pep8.StyleGuide()
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_docstring(self):
        """ Test doc strings
        """
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_inherits_BaseModel(self):
        """Test if the innstance is a subclas of BaseModel
        """
        self.assertTrue(issubclass(type(self.place1), BaseModel))

    def test_inicialization(self):
        """Test initizalition of the instance
        """
        self.assertTrue(hasattr(self.place1, "city_id"))
        self.assertIsInstance(self.place1.city_id, str)
        self.assertTrue(self.place1.city_id == "")
        self.assertTrue(hasattr(self.place1, "user_id"))
        self.assertIsInstance(self.place1.user_id, str)
        self.assertTrue(self.place1.user_id == "")
        self.assertTrue(hasattr(self.place1, "name"))
        self.assertIsInstance(self.place1.name, str)
        self.assertTrue(self.place1.name == "")
        self.assertTrue(hasattr(self.place1, "description"))
        self.assertIsInstance(self.place1.description, str)
        self.assertTrue(self.place1.description == "")
        self.assertTrue(hasattr(self.place1, "number_rooms"))
        self.assertIsInstance(self.place1.number_rooms, int)
        self.assertTrue(self.place1.number_rooms == 0)
        self.assertTrue(hasattr(self.place1, "number_bathrooms"))
        self.assertIsInstance(self.place1.number_bathrooms, int)
        self.assertTrue(self.place1.number_bathrooms == 0)
        self.assertTrue(hasattr(self.place1, "max_guest"))
        self.assertIsInstance(self.place1.max_guest, int)
        self.assertTrue(self.place1.max_guest == 0)
        self.assertTrue(hasattr(self.place1, "price_by_night"))
        self.assertIsInstance(self.place1.price_by_night, int)
        self.assertTrue(self.place1.price_by_night == 0.0)
        self.assertTrue(hasattr(self.place1, "latitude"))
        self.assertIsInstance(self.place1.latitude, float)
        self.assertTrue(self.place1.latitude == 0.0)
        self.assertTrue(hasattr(self.place1, "longitude"))
        self.assertIsInstance(self.place1.longitude, float)
        self.assertTrue(self.place1.longitude == 0.0)
        self.assertTrue(hasattr(self.place1, "amenity_ids"))
        self.assertIsInstance(self.place1.amenity_ids, list)
        self.assertTrue(self.place1.amenity_ids == [])


if __name__ == "__main__":
    unittest.main()
