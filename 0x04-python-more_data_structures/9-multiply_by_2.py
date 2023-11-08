#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_a_dictionary = a_dictionary.copy()
    for key in new_a_dictionary:
        value = new_a_dictionary[key]
        new_a_dictionary[key] = value * 2
    return new_a_dictionary
