#!/usr/bin/python3
"""The Base class"""
import json


class Base:
    """Defines the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                return f.write([])

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if type(json_string) != str or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set:"""
        if cls.__name__ == "Rectangle":
            dummy_attr = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_attr = cls(1)
        dummy_attr.update(**dictionary)
        return dummy_attr

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list_items = []
        return list_items
