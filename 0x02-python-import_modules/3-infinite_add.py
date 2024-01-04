#!/usr/bin/python3
if__name__ == "__main__":
    from sys import argv
    sumit = 0
    for i in range(1, len(argv)):
        sumit += int(argv[i])
    print("{}".format(sumit))