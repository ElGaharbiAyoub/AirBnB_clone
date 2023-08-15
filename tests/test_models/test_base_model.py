#!/usr/bin/python3
""" Tests for class BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models


class TestBaseModel(unittest.TestCase):
    """ Tests for class BaseModel """

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

    # def test_init_with_kwargs(self):
    #     now = datetime.now()
    #     kwargs = {
    #         'id': '123',
    #         'created_at': now.isoformat(),
    #         'updated_at': now.isoformat(),
    #         'custom_attr': 'custom_value'
    #     }
    #     model = BaseModel(**kwargs)
    #     self.assertEqual(model.id, kwargs['id'])
    #     self.assertEqual(model.created_at, now)
    #     self.assertEqual(model.updated_at, now)
    #     self.assertFalse(hasattr(model, 'custom_attr'))


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
