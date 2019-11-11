#!/usr/bin/env python3

#########################################################
# Created By: Pushtakio
# Purpose: generate general file for python development
# Date: 11/11/2019
# Version: 1.0.0
#########################################################

import os
import sys

#file_name=input("Please provide file name")

## Variables ::::::::::::::::::::::::::::::::::::::::::::::::::::::::

msg_exists = "The filename you choose, already exists in current folder:\
Pleae choose different name or move other folder"


string_data = '''
#!/usr/bin/env python3

#########################################################
# Created By: Pushtakio
# Purpose: 
# Date: 
# Version: 1.0.0
#########################################################
'''

line = "##########################################################"

## Funcs /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\


def deco(var):
    print(line, '\n', '#', var, '\n', line)


#####
# Main  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
#####

if __name__ == "__main__":
    file_name = sys.argv[1]
    print(file_name)
    file_name = input("Please provide file name")
    #if file_name == '':
    current_dir = os.getcwd()
    #if os.path.exists(current_dir):
    #        if os.path.exists(file_name):
    #            deco(msg_exists)
    #            sys.exit(1)
    #else:
    with open(file_name, 'x') as f:
        f.write(string_data)
    os.chmod(f'{file_name}', 0o775)


        
    

