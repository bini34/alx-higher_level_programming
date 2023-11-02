#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or idx > length:
        return None
    for i in my_list:
        if i - 1 == idx:
            return my_list[i - 1]
