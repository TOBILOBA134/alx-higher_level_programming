#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for add in set(my_list):
        result += add
    return result
