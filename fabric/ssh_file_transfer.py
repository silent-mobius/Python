#!/usr/bin/env python3
###############################################################################
# Python Network Programming Cookbook -- Chapter - 7
# This program is optimized for Python 3.7.
# It may run on any other version with/without modifications.
###############################################################################
# created by: Pushtakio
# purpose: practice fabric scripting
# date: 19/10/2019
# version: 1.0.1
###############################################################################


import os
import sys
import time
from getpass import getpass
try:
    from fabric.api import local, run, env, get, put, prompt, open_shell
except ModuleNotFoundError:
    print("fabric lib missing --> ",end='\t')
    time.sleep(0.5)
    print("\t trying to install: ")
    time.sleep(0.5)
    os.system('pip install fabric')
    print("try running the script once again")

def remote_server():
    env.hosts = ['127.0.0.1']
    env.password = getpass('Enter your system password: ')
    env.home_folder = '/tmp'


def login():
    open_shell(command="cd %s" %env.home_folder)

def download_file():
    print "Checking local disk space..."
    local("df -h")
    remote_path = prompt("Enter the remote file path:")
    local_path = prompt("Enter the local file path:")
    get(remote_path=remote_path, local_path=local_path)
    local("ls %s" %local_path)

def upload_file():
    print "Checking remote disk space..."
    run("df -h")
    local_path = prompt("Enter the local file path:")
    remote_path = prompt("Enter the remote file path:")
    put(remote_path=remote_path, local_path=local_path)
    run("ls %s" %remote_path)
