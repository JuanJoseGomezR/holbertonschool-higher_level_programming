#!/usr/bin/python3
"""reads a text file
"""


def read_file(filename=""):
    """reads file

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
    """
    with open(filename, encoding='utf-8') as file:
        read_cont = file.read() 
        print(read_cont, end='')
