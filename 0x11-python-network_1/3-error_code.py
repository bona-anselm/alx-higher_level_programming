#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8). It
    also manages urllib.error.HTTPError exceptions and print: Error
"""

import sys
from urllib import request, error


if __name__ == '__main__':
    url = sys.argv[1]

    sent_request = request.Request(url)

    try:
        with request.urlopen(sent_request) as resp:
            resp_body = resp.read()('utf-8')

            print(resp_body)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
