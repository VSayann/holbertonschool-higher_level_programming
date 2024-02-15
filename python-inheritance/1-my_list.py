#!/usr/bin/python3
"""
class inherates of list
"""


class MyList(list):
    """
    class that print sorted list

    Args:
        list: list to sorted and print
    """
    def print_sorted(self):
        """
        method for print a sorted list
        """
        print(sorted(self))
