#!/usr/bin/python3
""" Module Unittest for BaseModel """

import pep8
from unittest import TestCase
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """ test class BaseModel """

    def test_A_pep8_conformance(self):
        """Test that we conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            'models/base_model.py', 'tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
