#!/usr/bin/python3
"""
    A script that fetches https://alx-intranet.hbtn.io/status using the
    urllib package
"""

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as r:
    data = r.read()

print("Body response:\n\t - type: {}\n\t - content: {}\n\t - utf8 content: {}".format(type(data), data, data.decode('utf-8')))
