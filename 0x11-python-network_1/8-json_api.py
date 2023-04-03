#!/usr/bin/python3
"""
    Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    response = requests.post(
                             "http://e73beee7b20a.b72d3394.alx-cod. \
                             online:5000/search_user",
                             data={"q": q})

    try:
        json_response = response.json()
        if len(json_response) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_response["id"], json_response["name"]))
    except ValueError:
        print("Not a valid JSON")
