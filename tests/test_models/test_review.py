#!/usr/bin/python3
""" Module Unittest for Review """

import pep8
from unittest import TestCase
from models.base_model import BaseModel
from models.review import Review


class TestReview(TestCase):
    """ test class City """
    @classmethod
    def setUpClass(cls):
        """Define all attributes for test the class methods
        """
        cls.review = Review()

    @classmethod
    def tearDownClass(cls):
        """After run the Test clase remove the instance create
        for the test
        """
        del cls.review

    def test_pep8_conformance(self):
        """Test that we conforms to PEP8.
        """
        style = pep8.StyleGuide()
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "Fix pep8")

    def test_docstring(self):
        """ Test doc strings
        """
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_inherits_BaseModel(self):
        """Test if the innstance is a subclas of BaseModel
        """
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_inicialization(self):
        """Test initizalition of the instance
        """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertIsInstance(self.review.state_id, str)
        self.assertTrue(self.review.state_id == "")
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertIsInstance(self.review.user_id, str)
        self.assertTrue(self.review.user_id == "")
        self.assertTrue(hasattr(self.review, "text"))
        self.assertIsInstance(self.review.text, str)
        self.assertTrue(self.review.text == "")


if __name__ == "__main__":
    unittest.main()
