#!/usr/bin/pyhton3
def search_replace(my_list, search, replace):
    update_list = my_list[:]
    for elm in range(len(update_list)):
        if update_list[elm] == search:
            update_list[elm] = replace
    return (update_list)
