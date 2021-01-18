#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    aux_dic = a_dictionary.copy()
    for i, j in aux_dic.items():
        aux_dic[i] = j * 2
    return aux_dic
