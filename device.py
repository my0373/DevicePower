#!/usr/bin/env python3

"""
Author: Matt York

Mail: my0373@gmail.com

Description: This script is just a stub script to show how you could get or set
a bitmask for a device. 

There is some validation of the input bitmask (using some simple regex) and
command line options are all parsed using the argparse module.

Usage: 

# To get the status of the devices (return the bitmask)
./device.py 

# To set the status of the device (set the bitmask)
./device.py -m 01010101

Upon a successful run we exit with status code 0
Upon a failure (where handled) we exit with an exit status of >1
"""

import argparse
import re
import sys


def parseArgs():
    """
    Here we parse the arguments from the command line. 
    we have only one option --mask.

    """
    parser = argparse.ArgumentParser(description='Device')
    parser.add_argument('-m', '--mask', metavar='bitmask', type=str, nargs='?',
                        help='The device bitmask')

    args = parser.parse_args()

    return args


def readPins():
    """ 
    This is just a stub to simulate reading the state of the pins and 
    returning a mask.
    """
    pins = "01010101"
    return pins


def setPins(mask):
    """
    Here we set the mask, but only if the mask can be validated.
    """
    if validateMask(mask):
        print("mask is valid")
        print("Setting pins to :", mask)
        sys.exit(0)
    else:
        print("mask is invalid: Aborting")
        sys.exit(1)


def validateMask(mask):
    """
    Here we validate the bitmask string is exactly 8 characters and 
    contains only '0' or '1'.

    The returned value can be evaluated as True or False 
    """
    bre = re.compile('^[01]{8}$')

    return bre.match(mask)


if __name__ == '__main__':
    """
    This is the start of the script when run from the command line.
    """

    # Collect and parse the command line arguments
    args = parseArgs()

    # If the mask argument is empty, we just display the current state.
    # otherwise, if the mask is set we attempt to set it.
    if not args.mask:
        print(readPins())
        sys.exit(0)
    else:
        setPins(args.mask)
