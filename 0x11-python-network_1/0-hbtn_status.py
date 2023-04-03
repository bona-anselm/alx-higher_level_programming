#!/usr/bin/python3
"""
    A script that fetches https://alx-intranet.hbtn.io/status using the
    urllib package
"""

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as r:
    data = r.read()

print(f"Body response:")
print(f"\t - type: {type(data)}")
print(f"\t - content: {data}")
print(f"\t - utf8 content: {data.decode('utf-8')}")
