import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    print("Number of argument(s):", num_args)
    if num_args == 0:
        print(".", end="\n")
    else:
        print(":", end="\n")
        for i, arg in enumerate(args):
            print(i + 1, ":", arg)
