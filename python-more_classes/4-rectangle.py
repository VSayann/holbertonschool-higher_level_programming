#!/usr/bin/python3

"""defines a rectangle"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle.

        Args:
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter.

        Args:
            value (int): width value.
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter.

        Args:
            value (int): height value.
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        """instance method for get the area"""
        return self.width * self.height

    def perimeter(self):
        """instance method for get the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.width * 2 + self.height * 2

    def __str__(self):
        """instance method for the representation of strings of rectangle"""
        rectangle_string = ""
        if self.width == 0 or self.height == 0:
            return ""

        for index_a in range(self.height):
            for index_b in range(self.width):
                rectangle_string += "#"
            rectangle_string += "\n"

        return rectangle_string[:-1]

    def __repr__(self):
        """instance method for the printable representation of an object"""
        return f'Rectangle({self.width}, {self.height})'
