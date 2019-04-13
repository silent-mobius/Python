#!/usr/bin/env pyhton3

#json example
import os
import sys
import time
import csv


with open('csv_example.csv') as f:
	print(f.read())

time.sleep(1)
with open('csv_example.csv') as f:
	csv_python = csv.reader(f)
	
	fori in csv_python:
		print(f' device {i[0]} is in {i[2]} \
				and has ip {i[1]}')
