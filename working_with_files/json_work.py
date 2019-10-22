#!/usr/bin/env pyhton3

#json example
import os
import sys
import time
import json


with open('json_example.json') as f:
	json_ex = f.read
	
	

json_dict = json_loads(json_ex)


int_name = json_dict['interface']['name']


json_dict['interface']['name']['address']['ip']='10.0.10.100'

back_to_json = json.dumps(json_dict)

