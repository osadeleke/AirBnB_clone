#!/usr/bin/python3
"""
This module defines a class for data
serialization and deserialization
"""

import json
from os import path


class FileStorage():
    """
    Provides methods for data serialization and deserialization
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Gets dictionary of objects

        Return:
            dict: dictionary of objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds an object to a dictionary

        Args:
            obj (object): the object to be added
        """
        classname_id = type(obj).__name__ + "." + str(obj.id)
        FileStorage.__objects[classname_id] = obj

    def save(self):
        """
        Saves dictionary of objects to a file
        """
        obj_dict = {}
        for obj in FileStorage.__objects:
            obj_dict[obj] = FileStorage.__objects[obj].to_dict()
        with open(FileStorage.__file_path, mode="w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Reloads dictionary of objects from a file
        """
        if path.isfile(FileStorage.__file_path):
            obj_dict = {}
            with open(FileStorage.__file_path, mode="r") as file:
                obj_dict = json.load(file)
            from models.base_model import BaseModel
            from models.user import User
            # add here
            from models.state import State
            from models.amenity import Amenity
            for obj in obj_dict:
                if obj.startswith("BaseModel"):
                    FileStorage.__objects[obj] = BaseModel(**obj_dict[obj])
                elif obj.startswith("User"):
                    FileStorage.__objects[obj] = User(**obj_dict[obj])
                elif obj.startswith("State"):
                    FileStorage.__objects[obj] = State(**obj_dict[obj])
                elif obj.startswith("Amenity"):
                    FileStorage.__objects[obj] = Amenity(**obj_dict[obj])
