#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        cval = ord(str[i])
        upcar = chr(cval - 32)
        print("{}".format(upcar) if cval >= 97 and
              cval <= 122 else "{}".format(str[i]), end="")
    print()
