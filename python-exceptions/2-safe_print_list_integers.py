#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    number_elements = 0
    try:
        for index in range(0, x):
            if (isinstance(my_list[index], int)):
                print("{:d}".format(my_list[index]), end="")
                number_elements += 1
    except (TypeError):
        pass
    print()
    return number_elements
