#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx > length - 1:
        return my_list
    else:
        mylist = my_list.copy()
        mylist[idx] = element
        return mylist
