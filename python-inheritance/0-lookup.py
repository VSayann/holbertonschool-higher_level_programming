#!/usr/bin/python3
"""Defines an object attribute for lookup fonction"""


def lookup(obj):
    """ Return the list of availables attributes and methos of an object
    Args:
        obj: object to look up
    Returns:
        list of attributes and methods
    """
    return dir(obj)
