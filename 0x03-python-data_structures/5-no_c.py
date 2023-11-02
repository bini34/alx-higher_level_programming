#!/usr/bin/python3
def no_c(my_string):
    mystring = ''.join([char for char in my_string if char not in 'cC'])
    return mystring
