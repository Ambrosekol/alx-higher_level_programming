#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print("{}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print("\n" if ord(str[i]) < 65 and
                  ord(str[i]) > 90 else "{}".format(str[i]), end="")
