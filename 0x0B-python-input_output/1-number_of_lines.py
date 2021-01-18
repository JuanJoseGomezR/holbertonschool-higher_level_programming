#!/usr/bin/python3
"""COUNT LINES IN TXT FILE
"""


def number_of_lines(filename=""):
    """Counts lines

    Keyword Arguments:
        filename {str} -- [text] (default: {""})
    """
    with open(filename, encoding='utf-8') as file:
        count = 0
        for line in file:
            count += 1
    return(count)
