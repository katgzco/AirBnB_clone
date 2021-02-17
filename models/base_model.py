#!/usr/bin/python3
""" Module BaseModel """
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Constructot of atributes """

        if kwargs:
            if "created_at" in kwargs and type(kwargs["created_at"]) is str:
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "updated_at" in kwargs and type(kwargs["updated_at"]) is str:
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if "__class__" in kwargs:
                kwargs.pop("__class__")

            self.__dict__.update(kwargs)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ method that updates with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Method that return a dictionary containing
        all keys/values of __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """ Representation string of the information """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
