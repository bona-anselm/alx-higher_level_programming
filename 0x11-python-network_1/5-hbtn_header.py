#!/usr/bin/python3
""" A script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable found in the
    header of the response.
"""

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    with requests.get(url) as response:
        request_id = response.headers

        print(request_id.get('X-Request-Id'))
