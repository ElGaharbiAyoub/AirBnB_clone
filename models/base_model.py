#!/usr/bin/python3
""" Class BaseModel defines common attributes/methods for other classes """

import uuid
from datetime import datetime
import models


class BaseModel:
    """basemodel class"""

    def __init__(self, *args, **kwargs):
        """ Initilize a new instance of BaseModel class
        using arguments and keyword arguments"""

        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string representation of base model"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """saves the class"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of object"""
        dictt = dict(self.__dict__)
        dictt['__class__'] = str(self.__class__.__name__)
        dictt['created_at'] = self.created_at.isoformat()
        dictt['updated_at'] = self.updated_at.isoformat()
        return dictt
