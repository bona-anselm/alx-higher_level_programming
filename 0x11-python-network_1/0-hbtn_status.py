#!/usr/bin/python3
"""
    A script that fetches https://alx-intranet.hbtn.io/status using the
    urllib package
"""
from urllib import request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    with request.urlopen(url) as r:
        data = r.read()

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('utf-8')))
