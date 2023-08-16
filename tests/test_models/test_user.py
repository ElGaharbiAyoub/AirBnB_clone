#!/usr/bin/python3
""" Tests for class User """
import unittest
from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """ Tests for class User """

    def __init__(self, *args, **kwargs):
        """ Inititialize models to test """

        super().__init__(*args, **kwargs)
        self.test_class = User
        self.test_name = 'User'

    def test_attributes(self):
        """Test User attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str_representation(self):
        """Test the __str__ method"""
        user = User()
        str_rep = str(user)
        self.assertIsInstance(str_rep, str)
        self.assertIn("[User]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)


if __name__ == '__main__':
    unittest.main()
