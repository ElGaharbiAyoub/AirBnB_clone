#!/usr/bin/python3
"""
serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dataJson = {}
        for key, value in self.__objects.items():
            dataJson[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(dataJson, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

                for key, obj_data in data.items():
                    class_name = obj_data.pop('__class__')
                    obj_class = globals().get(class_name)
                    if obj_class is not None:
                        obj_instance = obj_class(**obj_data)
                        FileStorage.__objects[key] = obj_instance
                    else:
                        print(
                            "Warning: Class '{}' not found, skipping object."
                            .format(class_name))

        except FileNotFoundError:
            pass
