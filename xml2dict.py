#!/usr/bin/env pyhton3

#xmltodict example
import os
import sys
import time

try:
	print('library missing --> will try to install:')
	time.sleep(1)
	os.system('sudo pip3 install --user xmltodict')
except Exception as e:
	print(f'Error  occured')
	time.sleep(1)
	print(f'Error  details: {e}')

with open('xml_example.xml') as f:
	xml_example = f.read()
	
xml_dict = xmltodict.parse(xml_example)
	
int_name = xml_dict['interface']['name']

print(int_name)

xml_dict['interface']['name']['address']['ip']='10.0.10.100'

print(xmltodict.unparse(xml_dict))
