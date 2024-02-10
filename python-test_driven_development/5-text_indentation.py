#!/usr/bin/python3

"""print a text with 2 new lines after . ? and :"""


def text_indentation(text):
    """
        Arg:
            text: the text to print

        Raise:
            TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        if char == "." or char == "?" or char == ":":
            print(char)
            print()
        else:
            print(char, end="")
