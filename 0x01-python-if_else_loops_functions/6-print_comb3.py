#!/usr/bin/python3
for i1 in range(0, 9):
    for i2 in range(i1 + 1, 10):
        if (i1 == 8 and i2 == 9):
            print("{:d}{:d}".format(i1, i2))
        else:
            print("{:d}{:d}, ".format(i1, i2), end='')
