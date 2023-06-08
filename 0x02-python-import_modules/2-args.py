#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    count = len(argv)
    if count == 1:
        count = 0
    print("{} arguments:".format(count - 1) if count > 0
          else "{} arguments.".format(count))
    if count > 0:
        for val in range(1, count):
            print("{}: {}".format(val, argv[val]))
