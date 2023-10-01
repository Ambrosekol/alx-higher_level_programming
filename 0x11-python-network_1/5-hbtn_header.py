#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the
response header
"""

if __name__ == "__main__":
    import sys as system
    import requests

    res = requests.get(system.argv[1])
    header = res.headers
    print(header.get('X-Request-Id'))
