#!/usr/bin/python3
""" A script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable found in the
    header of the response.
"""

import sys
from urllib import request

if __name__ == '__main__':
    url = sys.argv[1]

    sent_request = request.Request(url)

    with request.urlopen(sent_request) as response:
        request_id = response.headers.get('X-Request-Id')

        print(request_id)
