#!/usr/bin/python3
"""
This is a script that that fetches https://alx-intranet.hbtn.io/status
You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like
the following example (tabulation before -)
You must use a with statement
"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
    response = r.read()
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode('utf-8')))
