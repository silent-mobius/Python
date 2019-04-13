#!/usr/bin/env pyhton3

#json example
import os
import sys
import time
import yaml


with open('yaml_example.yaml') as f:
	yaml_example = f.read()


yaml_dict = yaml.load(yaml_dict)

int_name= yaml_dict['interface']['name']

yaml_dict['interface']['name']['ipv4']['address'][0]['ip']='10.0.10.101'

backtoyaml = yaml.dump(yaml_dict,default_flow_style=False)
