#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx > length:
        return my_list
    for i in my_list:
        if i - 1 == idx:
            my_list[i - 1] = element
            return my_list

