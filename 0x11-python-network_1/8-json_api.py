#!/usr/bin/python3
"""
    Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        q = {'q': ""}
    else:
        q = {'q': sys.argv[1]}

    response = requests.post("0.0.0.0:5000/search_user",
                             data=q)

    try:
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print(f'[{response.get["id"]}] {response.get["name"]}')
    except ValueError:
        print("Not a valid JSON")
