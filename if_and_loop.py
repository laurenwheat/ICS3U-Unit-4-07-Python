#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program displays all integers 1000-2000


def main():

    loop_counter = 0

    for loop_counter in range(1000, 2000 + 1):
        if loop_counter % 5 == 0:
            print("{0}".format(loop_counter))
        else:
            print("{0} ".format(loop_counter), end="")


if __name__ == "__main__":
    main()
