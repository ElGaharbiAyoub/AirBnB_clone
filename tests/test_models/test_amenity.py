#!/usr/bin/python3
""" Tests for class Amenity """
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_str_representation(self):
        """Test the __str__ method"""
        amenity = Amenity()
        str_rep = str(amenity)
        self.assertIsInstance(str_rep, str)
        self.assertIn("[Amenity]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)


if __name__ == '__main__':
    unittest.main()
