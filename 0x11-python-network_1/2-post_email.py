#!/usr/bin/python3
"""
    A Python script that takes in a URL and an email, sends a POST
    request to the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8)
"""

import sys
from urllib import request, parse


if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    encoding_data = parse.urlencode(email)
    encoding_data = encoding_data.encode('utf-8')

    sent_request = request.Request(url, encoding_data)

    with request.urlopen(sent_request) as resp:
        resp_body = resp.read().decode('utf-8')

        print(resp_body)
