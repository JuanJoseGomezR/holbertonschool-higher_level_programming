#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        largest = 0
        for a in a_dictionary:
            if largest < a_dictionary[a]:
                largest = a_dictionary[a]
        for b in a_dictionary:
            if a_dictionary[b] is largest:
                return b
    else:
        return None
