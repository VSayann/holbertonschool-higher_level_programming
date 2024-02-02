#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    number_elements = 0
    try:
        for index in range(0, x):
            print(my_list[index], end="")
            number_elements += 1

    except IndexError:
        pass
    finally:
        print()
    return number_elements
