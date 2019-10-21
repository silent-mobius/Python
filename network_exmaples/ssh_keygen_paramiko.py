#############################################################
# crated by :  Pushtakio
# purpose:autogenerate in a pythonic way a ssh key
# date: 21.10.2019
# version: 1.0.0
#############################################################

import os
import sys
from paramiko import ecdsakey



#####
#Main - _
#####

k = ecdsakey.ECDSAKey.generate()  # why not rsa ???

public_key = k.get_base64()

with open("key.pub", "w") as fp:
    fp.write(public_key)


with open("key.priv", "w") as fp:
    os.chmod(0o600, "key.priv")
    k.write_private_key(fp)