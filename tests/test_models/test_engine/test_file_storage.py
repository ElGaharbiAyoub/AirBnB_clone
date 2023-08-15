#!/usr/bin/python3
""" Tests for class fileStorage """
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the 'all' method of FileStorage"""
        pass

    def test_new(self):
        """Test the 'new' method of FileStorage"""
        model = BaseModel()
        self.storage.new(model)
        all_objects = self.storage.all()
        self.assertIn('BaseModel.{}'.format(model.id), all_objects)

    def test_save_reload(self):
        """Test saving and reloading using FileStorage"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage = None
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIn('BaseModel.{}'.format(model.id), all_objects)

    def test_save(self):
        """ Tests serializing objects to json file """
        pass

    def test_reload(self):
        """ Tests deserializing the json file """
        pass


if __name__ == '__main__':
    unittest.main()
