#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("{} arguments".format(0))
    elif count == 1:
        print("{} argument".format(1))
    else:
        print("{} arguments".format(count))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
