#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotients = []
    result = 0
    for a in range(list_length):
        try:
            result = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            quotients.append(result)
    return quotients
