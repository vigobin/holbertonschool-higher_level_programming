#!/usr/bin/python3
"""The student class"""


class Student:
    """Defines the student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) != list:
            return self.__dict__
        else:
            temp_dict = {}
            for i in attrs:
                temp_dict[i] = self.__dict__[i]
            return temp_dict

    def reload_from_json(self, json):
        for i in json.keys():
            self.__dict__[i] = json[i]
