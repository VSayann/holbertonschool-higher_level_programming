#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for line in matrix:
            for index in range(len(line)):
                if index == len(line) - 1:
                    print("{:d}".format(line[index]), end="")
                else:
                    print("{:d}".format(line[index]), end=" ")
            print()
    else:
        print()
