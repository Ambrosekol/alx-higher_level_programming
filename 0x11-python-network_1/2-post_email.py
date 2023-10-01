#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys as system
    import urllib.request as broswer
    import urllib.parse as parser

    url = system.argv[1]
    val = {
        'email' : '{}'.format(system.argv[2])
        }
    par = parser.urlencode(val)
    par = par.encode('ascii')
    reqst = broswer.Request(url, par)
    with broswer.urlopen(reqst) as response:
        res_val = response.read()
        print(res_val)
