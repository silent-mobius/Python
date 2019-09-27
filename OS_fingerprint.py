#!/usr/bin/env python3
########################################################################
# created by: Pushtakio
# purpose: practice os fingerprinting copied  and iptimized for python3 from aggressive python book.
# date: 01.03.2013
# version: 4
########################################################################

import platform
"""
Fingerprints the following Operating Systems:
* Mac OS X
* Ubuntu
* Red Hat/Cent OS
* FreeBSD
* SunOS
"""
class OpSysType(object):
	def __getattr__(self, attr):
		if attr == "osx":
			return "osx"
		elif attr == "rhel":
		  return "redhat"
		elif attr == "ubu":
		  return "ubuntu"
		elif attr == "fbsd":
		  return "FreeBSD"
		elif attr == "sun":
		  return "SunOS"
		elif attr == "unknown_linux":
		  return "unknown_linux"
		elif attr == "unknown":
		  return "unknown"
		else:
		  raise AttributeError, attr
		  
		  
	def linuxType(self):
		if platform.dist()[0] == self.rhel:
			return self.rhel
		elif platform.uname()[1] == self.ubu:
		  return self.ubu
		else:
		  return self.unknown_linux
	
	def queryOS(self):
		if platform.system() == "Darwin":
			return self.osx
		elif platform.system() == "Linux":
		  return self.linuxType()
		elif platform.system() == self.sun:
		  return self.sun
		elif platform.system() == self.fbsd:
			  return self.fbsd
			  
def fingerprint():
	type = OpSysType()
	print type.queryOS()
		
if __name__ == "__main__":
		fingerprint()
