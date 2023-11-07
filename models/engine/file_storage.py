#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes and deserializes instances
    """

    __file_path = "file.json"
    __objects = {}   # Stores all objects

    def all(self):
        """
        returns all objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        adds `obj` to  __objects dict
        """

        key = obj.__class__.__name__ + '.' + obj.id

        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to json file.
        """

        with open(FileStorage.__file_path, "w", encoding='utf-8') as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """
        loads json file to __objects.
        """

        try:
            with open(FileStorage.__file_path, "r", "utf-8") as json_file:
                FileStorage.__objects = json.load(json_file)

        except Exception:
            return

    def Classes(self):
        """
        dictionary of all classes
        """
        classes = {"BaseModel": BaseModel}
        
        return classes
