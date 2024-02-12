#!/usr/bin/python3
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ a class BaseModel that defines methods for other classes"""
    def __init__(self, *args, **kwargs):
        """initalize Public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            mynew_dict = {}
            for key, v in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        if isinstance(v, str):
                            datestyle = '%Y-%m-%dT%H:%M:%S.%f'
                            v = datetime.datetime.strptime(v, datestyle)
                    self.__dict__[key] = value
                    if 'id' not in kwargs:
                        self.__dict__['id'] = str(uuid.uuid4())
        else:
            storage = FileStorage()
            storage.new(self)

    def __str__(self):
        """return string"""
        name = self.__class__.__name__
        return ("[{}] ({}) {}".format(name, self.id, self.__dict__))

    def save(self):
        """save updated"""
        self.updated_at = datetime.datetime.now()
        FileStorage.save()

    def to_dict(self):
        """return to dictionary"""
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['create_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
