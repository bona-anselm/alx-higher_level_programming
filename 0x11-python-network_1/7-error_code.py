#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8). It
    also manages urllib.error.HTTPError exceptions and print: Error
"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]

    request_resp = requests.get(url)

    if request_resp.status_code < 400:
        print(request_resp.text)
    else:
        print(f"Error code: {request_resp.status_code}")
