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
    from fabric.contrib.files import exists
except ModuleNotFoundError:
    print("fabric lib missing --> ",end='\t')
    time.sleep(0.5)
    print("\t trying to install: ")
    time.sleep(0.5)
    os.system('pip install fabric')
    print("try running the script once again")



WWW_DOC_ROOT = "/data/apache/test/" # needs fixing !!!
WWW_USER = "apache2"
WWW_GROUP = "apache2"
APACHE_SITES_PATH = "/var/www/html"
APACHE_INIT_SCRIPT = "/etc/init.d/apache2 "



def remote_server():
    env.hosts = ['127.0.0.1']
    env.user = prompt('Enter user name: ')
    env.password = getpass('Enter your system password: ')

def setup_vhost():
    """ Setup a test website """
    print ("Preparing the Apache vhost setup...")
    print ("Setting up the document root...")
    if exists(WWW_DOC_ROOT):
        sudo(f"rm -rf %{WWW_DOC_ROOT}")
        sudo(f"mkdir -p {WWW_DOC_ROOT}") # setup file permissions
        sudo(f"chown -R {env.user}:{env.user} {WWW_DOC_ROOT}") # upload a sample index.html file
        put(local_path="index.html", remote_path=WWW_DOC_ROOT)
        sudo(f"chown -R {WWW_USER}:{WWW_GROUP} {WWW_DOC_ROOT}")
        print("Setting up the vhost...")
        time.sleep(0.5)
        sudo(f"chown -R {env.user}:{env.user} {APACHE_SITES_PATH}") # upload a pre-configured vhost.conf
        put(local_path="vhost.conf", remote_path=APACHE_SITES_PATH)
        sudo(f"chown -R {'root'}:{'root'} {APACHE_SITES_PATH}" # restart Apache to take effect
        sudo(f"{APACHE_INIT_SCRIPT} restart")
        print "Setup complete. Now open the server path http://abc.remote-server.org/ in your web browser."
