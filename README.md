# DevicePower
Some example python and ansible playbooks to demonstrate how you might control Arduino pins via Ansible and Python.

## To test
    ansible-playbook -i inventory ./device.py

## To use device.py
This script is just a stub script to show how you could get or set
a bitmask for a device. 

There is some validation of the input bitmask (using some simple regex) and
command line options are all parsed using the argparse module.

Usage: 

#### To get the status of the devices (return the bitmask)
    ./device.py 

#### To set the status of the device (set the bitmask)
    ./device.py -m 01010101

Upon a successful run we exit with status code 0
Upon a failure (where handled) we exit with an exit status of >1
