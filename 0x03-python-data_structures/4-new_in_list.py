#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mylist = my_list.copy()
    length = len(mylist)
    if idx < 0 or idx > length:
        return mylist
    for i in mylist:
        if i - 1 == idx:
            mylist[i - 1] = element
            return mylist
