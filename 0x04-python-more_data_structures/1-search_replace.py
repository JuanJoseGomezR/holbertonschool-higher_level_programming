#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
        _replacing = my_list[i]
        if _replacing is search:
            _replacing = replace
        new_list.append(_replacing)
    return new_list
