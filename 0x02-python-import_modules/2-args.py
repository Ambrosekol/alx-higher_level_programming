#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = sys.argv.__len__()
    argv = sys.argv
    if argc == 1:
        argc = 0
    print("{} arguments:".format(argc - 1) if argc > 0
          else "{} arguments.".format(argc))
    if argc > 0:
        for val in range(1, argc):
            print("{}: {}".format(val, argv[val]))
    