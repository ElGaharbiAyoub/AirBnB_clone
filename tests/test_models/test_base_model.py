#!/usr/bin/python3
""" Tests for class BaseModel """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import models
import os
import os.path


class TestBaseModel(unittest.TestCase):
    """ Tests for class BaseModel """

    def __init__(self, *args, **kwargs):
        """ Inititialize models to test """

        super().__init__(*args, **kwargs)
        self.test_class = BaseModel
        self.test_name = 'BaseModel'

    def test_init(self):
        """Tests for init """
        model = BaseModel()
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_str(self):
        """Test __str__ method"""
        model = BaseModel()
        str_repr = str(model)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn("id", str_repr)
        self.assertIn("created_at", str_repr)
        self.assertIn("updated_at", str_repr)

    def test_save_load(self):
        """ Tests save and reload """

        if os.path.exists('file.json'):
            os.remove('file.json')
        _save = FileStorage()
        _save.reload()
        _object = self.test_class()
        self.assertTrue(self.test_name + '.' + _object.id in _save.all())

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], "BaseModel")
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)
        self.assertEqual(type(model_dict['id']), str)

    def test_save_existing_instance(self):
        """Test saving a existing instance from dictionary"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        key = 'BaseModel.{}'.format(model.id)
        self.assertEqual(models.storage.all()[key], model)
        new_updated_at = models.storage.all()[key].updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == '__main__':
    unittest.main()
