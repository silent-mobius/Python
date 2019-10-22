#!/usr/bin/env python3
###############################################################################
# Python Network Programming Cookbook -- Chapter - 7
# This program is optimized for Python 3.6
# It may run on any other version with/without modifications.
###############################################################################
# created by: Pushtakio
# purpose: practice fabric scripting
# date: 19/10/2019
# version: 1.0.1
########################################################################

import os
import sys
import time
from getpass import getpass

try:
    from fabric.api import settings, run, env, prompt

except ModuleNotFoundError:
    print("fabric lib missing --> ")
    time.sleep(0.5)
    print("trying to install: ")
    time.sleep(0.5)
    os.system('pip install fabric')
    print("try running the script once again")

def remote_server():
    env.hosts = ['127.0.0.1']
    env.user = prompt('Enter user name: ')
    env.password = getpass('Enter password: ')

def install_package():
    run("pip3 install yolk")
