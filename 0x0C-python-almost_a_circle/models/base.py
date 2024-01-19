#!/usr/bin/python3
"""Defines a class"""

import json
from collections import OrderedDict


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for Base class."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        ordered_dicts = [
                OrderedDict(obj.items())
                for obj in list_dictionaries
                ]
        return json.dumps(ordered_dicts, separators=(',', ':'))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        json_str = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]
                )
        with open(filename, 'w') as file:
            file.write(json_str)
