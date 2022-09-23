#!/usr/bin/python3
"""A script that takes 2 arguments.
The first argument will be the repository name.
The second argument will be the owner name in order.
You must use the packages requests and sys """
import requests
from sys import argv


if __name__ == '__main__':
    try:
        url = requests.get('https://api.github.com/repos/{}/{}/comits'
                           .format(argv[2], argv[1]))
        response = requests.get(url)
        json_obj = response.json()
        for i, obj in enumerate(json_obj):
            if i == 10:
                break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print("{}: {}".format(obj.get('sha'), name))
    except ValueError as invalid_json:
        pass
