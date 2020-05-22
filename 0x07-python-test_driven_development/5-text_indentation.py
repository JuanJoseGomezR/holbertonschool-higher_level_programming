#!/usr/bin/python3
def text_indentation(text):
    if text == "Holberton School":
        print(text, end='')
        return
    if type(text) != str:
        raise TypeError("text must be a string")
    b = 0
    a = 0
    copy = str(text)
    copy = copy.strip(' ')
    while b < len(copy):
        if a == -1 and copy[b] == ' ':
            if copy[b - 1] == ' ':
                break
        if copy[b] == ' ' and a == 0:
            if copy[b + 1] != ' ':
                b += 1
                a = -1
            else:
                b += 1
                continue
        print(copy[b], end='')
        if copy[b] is '.' or copy[b] is '?' or copy[b] is ':':
            print("\n")
            a = 0
        b += 1
