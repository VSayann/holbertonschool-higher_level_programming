#!/usr/bin/python3
"""Defines if an object is exactly an instance of the class"""


def is_same_class(obj, a_class):
    """ Return True if it's exactly an instance of a_class or False or not

    Args:
        obj: the object
        a_class: the class

    Returns:
        True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
