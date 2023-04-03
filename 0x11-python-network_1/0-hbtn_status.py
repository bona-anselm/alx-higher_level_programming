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

    print(f"Body response:\n\t - type: {type(data)}\n\t"
          f" - content: {data}\n\t "
          f"- utf8 content: {data.decode('utf-8')}")
