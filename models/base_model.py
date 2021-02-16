#!/usr/bin/python3
import  uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Constructot of atributes """

        if len(kwargs) > 0:           
            #modifica
            self.__dict__.update(kwargs)
            
            if "created_at" in kwargs:
                #acceder a la llave y convertimos el string a datetime
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

            if "update_at" in kwargs:
                #acceder a la llave
                kwargs["update_at"] = datetime.strptime(kwargs["update_at"], "%Y-%m-%dT%H:%M:%S.%f")

            if "__class__" in kwargs:
                kwargs.pop("__class__")

        else:
            #crea
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
            models.storage.new(self)
    
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now().isoformat()
        models.storage.save()
    
    def to_dict(self):
        dictionary = self.__dict__
        dictionary.update({"__class__": self.__class__.__name__})
        return dictionary
