#!/usr/bin/python3
""" Tests for class City """
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_str_representation(self):
        """Test the __str__ method"""
        city = City()
        str_rep = str(city)
        self.assertIsInstance(str_rep, str)
        self.assertIn("[City]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)


if __name__ == '__main__':
    unittest.main()
