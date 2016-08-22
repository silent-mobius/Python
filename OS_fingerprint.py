#!/usr/bin/env python

import platform

class OpSysType(Obj):
	
	
	
	def __getattr__(self,attr):
		if attr = 'osx':
			return 'osx'
		elif attr = 'rhel':
			return 'RedHat'
		elif attr = 'ubu':
			return 'Ubuntu'
		elif attr = 'fbsd':
			return 'FreeBSD'
		elif attr = 'sun':
			return 'SunOS'
		elif attr = 'unknown_linux':
			return 'unknown_linux'
		elif attr = 'unknown':
			return 'unknown'
		else:
			raise AttributeError, attr
			
			
	def linuxType(self):
		if platform.dist()[0] == self.rhel:
			return self.rhel
		elif platform.uname()[1] == self.ubu:
			return self.ubu
		#TODO add as much distro as possible.
		else:
			return self.unknown_linux
			
			
	def queryOS(self):
		if platform.system() == 'Darwin':
			return self.osx
