# !/usr/bin/env python3

# Created by Trent Hodgins
# Created on 09/14/2020
# This program calculates the circumference of a circle
# The user enters the radius

import constants_2_03


def main():
    # This calculates the circumference

    # input
    radius = int(input("Enter radius of the circle (mm): "))

    # process
    circumference = constants_2_03.TAU * radius

    # output
    print("Circumference is {} mm2.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
