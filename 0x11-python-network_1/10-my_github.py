#!/usr/bin/python3
""" gittu hubbu """
import sys
import requests


if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = requests.get('https://api.github.com/user', auth=(a, b))
    print(c.json().get('id'))
