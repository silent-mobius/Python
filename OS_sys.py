#!/usr/bin/env python3
########################################################################
# created by: Pushtakio
# purpose: testing file
# date: 10.02.2018
# version: 1.0.1
########################################################################


import platform

profile = [
platform.architecture(),
platform.dist(),
platform.libc_ver(),
platform.mac_ver(),
platform.node(),
platform.platform(),
platform.processor(),
platform.python_build(),
platform.python_compiler(),
platform.python_version(),
platform.system(),
#platform.uname(),
platform.version(),
]

for p in profile:
	print(p)
