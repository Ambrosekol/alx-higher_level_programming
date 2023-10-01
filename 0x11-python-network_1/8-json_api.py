#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    parameters = {
        'q': ""
    }
    if len(argv) > 1:
        parameters["q"] = argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data=parameters)
    try:
        j_data = req.json()
        id, name = j_data.get('id'), j_data.get('name')
        if len(j_data) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}]: {}".format(id, name))
    except requests.JSONDecodeError as e:
        print("Not a valid JSON")
