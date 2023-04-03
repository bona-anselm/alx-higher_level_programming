#!/usr/bin/python3
"""
    A script that fetches https://alx-intranet.hbtn.io/status using the
    urllib package
"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    with requests.get(url) as r:
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
