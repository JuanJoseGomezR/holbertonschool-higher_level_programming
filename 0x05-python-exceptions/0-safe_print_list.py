#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    prints = 0
    for a in range(0, x):
        try:
            print("{}".format(my_list[a]), end='')
            prints += 1
        except:
            break
    print()
    return prints
