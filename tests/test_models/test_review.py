#!/usr/bin/python3
""" Tests for class Review"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for the Review class"""


    def test_attributes(self):
        """Test Review attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


    def test_str_representation(self):
        """Test the __str__ method"""
        review = Review()
        str_rep = str(review)
        self.assertIsInstance(str_rep, str)
        self.assertIn("[Review]", str_rep)
        self.assertIn("'id':", str_rep)
        self.assertIn("'created_at':", str_rep)
        self.assertIn("'updated_at':", str_rep)

if __name__ == '__main__':
    unittest.main()
