#!/usr/bin/python3
""" Tests for class Place """
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def test_attributes(self):
        """Test Place attributes"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_str_representation(self):
        """Test the __str__ method"""
        place = Place()
        str_rep = str(place)
        self.assertIsInstance(str_rep, str)
        self.assertIn("[Place]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)


if __name__ == '__main__':
    unittest.main()
