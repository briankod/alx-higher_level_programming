"""A script that takes 2 arguments.
The first argument will be the repository name.
The second argument will be the owner name in order.
You must use the packages requests and sys """
import requests
from sys import argv


if __name__ == '__main__':
    url = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(argv[2], argv[1]))
    response = requests.get(url)
    try:
        json_obj = response.json()
        for i in range(10):
            print("{}: {}".format(json_obj[i]["sha"],
                                  json_obj[i]["commit"]["author"]["name"]))
    except IndexError:
        pass
