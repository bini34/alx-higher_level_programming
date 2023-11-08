#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    count = 0
    for i in new_list:
        new_list[count] = i * number
        count = count + 1
    return new_list
