#!/usr/bin/python3
from models.base_model import BaseModel
import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__,obj.id)
        FileStorage.__objects.update({key:obj})

    def save(self):
        dict_for_json = {}
        for key, value in FileStorage.__objects.items():
            dict_for_json[key] = value.to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as json_file_dump:
            json.dump(dict_for_json, json_file_dump, indent=2)


    def reload(self):
            try:
                with open(FileStorage.__file_path, mode="r", encoding="utf-8") as json_file_load:
                   for key, value in (json.loads(json_file_load)).items():
                        new_obj = eval(value["__class__"] + "(**value)")
                        FileStorage.__objects[key] = new_obj
            except BaseException:
                pass


