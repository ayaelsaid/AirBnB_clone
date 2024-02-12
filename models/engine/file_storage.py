#!/usr/bin/python3
import json
import os


class FileStorage:
    """
    recreate a BaseModel from another one
    Attributes:
        __file_path: file
        __objects: dictionary
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects"""
        clsnme = self.__class__.__name__
        key = f"{clsnme} {obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        for obj_id, obj in FileStorage.__objects.iteam():
            dicOFobj = obj.to_dict()
            dicOFobj[obj_id] = dicOFobj
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r") as f:
                    FileStorage.__objects = json.load(f)
        except FileNotFoundError as e:
            print(e)
