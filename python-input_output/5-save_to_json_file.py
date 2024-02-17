#!/usr/bin/python3

"""
write an object to a text file with a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ write text file in objects with a JSON representation

        Args:
            my_obj: the object
            filename: the name of the file
        Returns:
            the text file with JSON representation
    """
    json_object = json.dumps(my_obj)
    with open(filename, "w") as file:
        return file.write(json_object)
