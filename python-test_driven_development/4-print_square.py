#!/usr/bin/python3

"""print a square"""


def print_square(size):
    """
        Arg:
            size: the size of the square

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if not isinstance(size, int) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        print("#" * size)
