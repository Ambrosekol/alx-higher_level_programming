#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://github.com/users/{}".format(argv[1])
    req = requests.get(url, auth=(argv[1], argv[2]))
    print(req.json().get("id"))
