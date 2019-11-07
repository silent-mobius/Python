#!/usr/bin/env python3

################################################
#created by: Pushtakio
#puspose: connect to web server and validate port 80
#date:07/11/2019
#version: 1.0.0
################################################

import os
import sys
import sqlite3
from sqlite3 import Error
try:
    from fabric import Connection
except ModuleNotFoundError as e:
    print("Unable to import")
    print(e)


def create_remote_db():
    try:
        c = sqlite3.connect('remote.db')
        return c
    except Error:
        print(Error)

def create_remote_table_in(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE\
                employees(id integer PRIMARY KEY,\
                           name text, salary real,\
                           department text, position text,\
                           hireDate text)")
    cur.commit()

