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
    from fabric.api import settings, run, env, prompt

except ModuleNotFoundError:
    print("fabric lib missing --> ")
    time.sleep(0.5)
    print("trying to install: ")
    time.sleep(0.5)
    os.system('pip install fabric')
    print("try running the script once again")


def remote_server():
    env.hosts = ['127.0.0.1'] # Edit this list to include remote hosts
    env.user =prompt('Enter your system username: ')
    env.password = getpass('Enter your system user password: ')
    env.mysqlhost = 'localhost'
    env.mysqluser = 'root'prompt('Enter your db username: ')
    env.password = getpass('Enter your db user password: ')
    env.db_name = ''

def show_dbs():
    """ Wraps mysql show databases cmd"""
    q = "show databases"
    run(f"echo {q} | mysql -u{env.mysqluser} -p {env.mysqlpassword}")

def run_sql(db_name, query):
    """ Generic function to run sql"""
    with cd('/tmp'):
        run(f"echo {query} | mysql -u{env.mysqluser} -p{env.mysqlpassword} -D {db_name}")

def create_db():
    """Create a MySQL DB for App version"""
    if not env.db_name:
        db_name = prompt("Enter the DB name:")
    else:
        db_name = env.db_name
        run(f'echo "CREATE DATABASE {db_name} default character set utf8 collate utf8_unicode_ci;" | mysql --batch --user={env.mysqluser} --password={env.mysqlpassword} --host={env.mysqlhost}', pty=True)

def ls_db():
    """ List a dbs with size in MB """
    if not env.db_name:
        db_name = prompt("Which DB to ls?")
    else:
        db_name = env.db_name
        query = f"""SELECT table_schema "DB Name", Round(Sum(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB"
        FROM information_schema.tables WHERE table_schema = \"{db_name}\" GROUP BY table_schema """
        run_sql(db_name, query)


def empty_db():
    """ Empty all tables of a given DB """
    db_name = prompt("Enter DB name to empty:")
    cmd = f"""(echo 'SET foreign_key_checks = 0;';
    (mysqldump -u{env.mysqluser} -p{env.mysqlpassword} --add-drop-table --no-data {db_name} |grep ^DROP);
    echo 'SET foreign_key_checks = 1;') | mysql -u{env.mysqluser} -p{env.mysqlpassword} -b {db_name}"""
    run(cmd)
