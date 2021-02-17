#!/usr/bin/python3
""" Module FileStorage """
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    """ Class that serializes instances to JSON file
    and deserializes JSON file to instances
    Private class Atributes:
        __file_path (str): path with .json
        __objects   (dic): dictionary of dictionaries
    Public instance methods:
        all(), new(), save(), and reload()
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """
        set in __objects the obj with key <ob class name>.id
        Args:
        obj (dictionary):
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serialize __objects to the JSON file """
        dict_for_json = {}
        for key, value in self.__objects.items():
            dict_for_json[key] = value.to_dict()

        with open(self.__file_path, mode="w") as json_file_dump:
            json.dump(dict_for_json, json_file_dump, indent=2)

    def reload(self):
        """ Method that desearializes the JSON file to __objects """
        try:
            with open(self.__file_path, mode="r") as json_file_load:
                for key, value in (json.load(json_file_load)).items():
                    self.__objects[key] = eval(value["__class__"] +
                                               "(**value)")
        except BaseException:
            pass
