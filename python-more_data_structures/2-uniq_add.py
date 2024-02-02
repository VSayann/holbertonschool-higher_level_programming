#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    temp_list = []
    for index in range(len(my_list)):
        if my_list[index] not in temp_list:
            sum += my_list[index]
            temp_list.append(my_list[index])
    return sum
