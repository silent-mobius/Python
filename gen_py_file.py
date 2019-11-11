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


string_data='''
#!/usr/bin/env python3

#########################################################
# Created By: Pushtakio
# Purpose: 
# Date: 
# Version: 1.0.0
#########################################################
'''
line="##########################################################"
## Funcs /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
def deco(msg_string):
    print(line)
    print('#', msg_string)
    print(line)


#####
# Main  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
#####

if __name__ == "__main__":
    if sys.argv[1] == ' ':
        file_name = input("Please provide file name")
        current_dir = os.getcwd()
        if os.path.exists(f'{current_dir/file_name}'):
            deco(msg_exists)
        else:
            with open('{current_dir/file_name}','x') as f:
                f.write(string_data)


        
    

