#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    url = "https://api.github.com/users/{}".format(argv[1])
    req = requests.get(url, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(req.json().get("id"))
