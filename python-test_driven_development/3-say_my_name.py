#!/usr/bin/python3

"""print My name is with value of first_name and last_name"""


def say_my_name(first_name, last_name=""):
    """
        Args:
            first_name: first name of the person
            last_name: last name of the person

        Raises:
            TypeError: first_name must be a string
            TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
