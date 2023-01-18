#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if j > i:
            print("{}{}".format(i, j), end='')
            if i < 8:
                print(', ', end='')
            else:
                print()
