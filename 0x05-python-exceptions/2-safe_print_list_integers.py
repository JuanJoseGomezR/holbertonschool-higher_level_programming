#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    itere = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end='')
        except ValueError:
            continue
        except TypeError:
            continue
        itere += 1
    print()
    return itere
