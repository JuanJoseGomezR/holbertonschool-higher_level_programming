#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end='')
        except ValueError:
            continue
        except TypeError:
            continue
        printed += 1
    print()
    return printed
