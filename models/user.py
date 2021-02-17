#!/usr/bin/python3
""" Module First User """

from models.base_model import BaseModel

class User(BaseModel):
    """ Class that inherits from BaseModel
    Public class attributes:
        email (str)
        password (str)
        first_name (str)
        last_name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    