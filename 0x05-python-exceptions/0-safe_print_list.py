#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    itere = 0
    for a in range(0, x):
        try:
            print("{}".format(my_list[a]), end='')
            itere+= 1
        except:
            break
    print()
    return itere