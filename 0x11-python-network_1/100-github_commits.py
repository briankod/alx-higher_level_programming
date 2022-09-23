#!/usr/bin/python3
"""A script that takes 2 arguments.
The first argument will be the repository name.
The second argument will be the owner name in order.
You must use the packages requests and sys """
import requests
from sys import argv


if __name__ == '__main__':
    import requests
    from sys import argv
    url = requests.get('https://api.github.com/repos/{}/{}/comits'
                       .format(argv[2], argv[1]))
    response = requests.get(url)
    json_obj = response.json()
    for commit in json_obj[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
