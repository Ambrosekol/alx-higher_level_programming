#!/usr/bin/python3
for alph in range(ord('a'), ord('z') + 1):
    if alph == ord('q') or alph == ord('e'):
        continue
    print("{}".format(chr(alph)), end="")
