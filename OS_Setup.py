#!/usr/bin/env python

########################################################################
#Purpose : automating dev and proper working environment  installation
########################################################################
#Copyright (c) <2014-2016>, <LinuxSystems LTD>
#All rights reserved.
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the <LinuxSystems LTD> nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
#DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
########################################################################

#lib import
import os
import sys
import apt
import platform
import subprocess
import argparse


##Vars::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
var = platform.dist()
REPO = var[0]
USER = "mobius" ### place your user name here
PASSWD = "1"         ### palce your passwd here
REPONAME = var[0]
KODENAME = 
ARCH = platform.machine()
VERSION = var[1]
INSTALL_MNGR =
DISTROS = {
		"Ubuntu" : "/etc/lsb-release",
		"Debian" : "/etc/debian_version",
		"RedHat" : "/etc/redhat-release",
		"SUSE" : "/etc/SUSE-release",
		"Fedora" : "/etc/fedora-release",
		"Gentoo" : "/etc/gentoo-release",
		"Slackware" : "/etc/slackware-version",
		"Mandriva" : "/etc/mandriva-release",
		"Mandrake" : "/etc/mandrake-release",
		"YellowDog" : "/etc/yellowdog-release",
		"SUN JDS" : "/etc/sun-release",
	}
packages = ['lightdm','mate-desktop-environment-extras', 'firmware-realtek', 'firmware-linux', 'firmware-linux-free',
'firmware-linux-nonfree', 'vlc', 'gparted', 'abiword', 'transmission', 'guake', 'mixxx', 'culmus', 'xfonts-efont-unicode',
'xfonts-efont-unicode-ib', 'xfonts-intl-european', 'msttcorefonts', 'sqlite', 'sqlite3', 'mysql-client', 'mysql-server',
'postgresql', 'apache2', 'nginx-full', 'nfs-common', 'samba-common', 'redis-server', 'sysv-rc-conf', 'wget', 'curl', 'nmap',
'zenmap', 'aircrack-ng', 'dsniff', 'ndiff', 'nbtscan', 'wireshark', 'tshark', 'tcpdump', 'netcat', 'macchanger', 'python-scapy',
'python-pip', 'python-networkx', 'python-netaddr', 'python-netifaces', 'python-netfilter', 'python-gnuplot', 'python-mako',
'python-radix', 'ipython', 'python-pycurl', 'python-lxml', 'python-libpcap', 'python-nmap', 'python-flask', 'python-scrapy',
'libpoe-component-pcap-perl', 'libnet-pcap-perl', 'perl-modules', 'geany', 'build-essential', 'debhelper', 'cmake', 'bison',
'flex', 'libgtk2.0-dev', 'libltdl3-dev', 'libncurses-dev', 'libusb-1.0-0-dev', 'git', 'git-core', 'libncurses5-dev',
'libnet1-dev', 'libpcre3-dev', 'libssl-dev', 'libcurl4-openssl-dev', 'ghostscript', 'autoconf', 'python-software-properties',
'debian-goodies', 'freeglut3-dev', 'libxmu-dev', 'libpcap-dev', 'libglib2.0', 'libxml2-dev', 'libpcap-dev', 'libtool',
'rrdtool', 'autoconf', 'automake', 'autogen', 'redis-server', 'libsqlite3-dev', 'libhiredis-dev', 'libgeoip-dev',
'debootstrap', 'qemu-user-static', 'device-tree-compiler', 'lzma', 'lzop', 'pixz', 'dkms', 'gnupg', 'flex', 'bison', 'gperf',
'libesd0-dev', 'zip', 'curl', 'libncurses5-dev', 'zlib1g-dev', 'gcc-multilib', 'g++-multilib', 'libusb-1.0-0',
'libusb-1.0-0-dev', 'fakeroot', 'kernel-package', 'zlib1g-dev', 'devscripts', 'pbuilder', 'dh-make', 'mingw32',
'mingw32-binutils', 'guake']
pack_to_install = []
###Func/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

def bash(var):
	os.system(var)


'''def distrofind(discreet):

	for name,location in DISTROS.iteritems():
		try:
			distroFile = open("%s" % location,"r")
			content = distroFile.readlines(); distroFile.close();
			if discreet == 0:
				IDfile = open("%s/DistroID" % cwd,"a")
				IDfile.writelines(content); IDfile.close();
				print "The contents of the identification file has been created at"
				print "%s/DistroID for easy reference. You may use Python to " % cwd
				print "parse it and obtain advanced information about the user's OS."
			else: pass
			return name
		except IOError:
			issueFile = open("/etc/issue","r")
			issue = issueFile.readline(); issueFile.close()
			qname = issue.split(); issue = qname[0];
			return issue
'''
def edit_files():
	if 
	 
def pac_check(pkg):
	cache = apt.Cache()
	
	pack = cache[pkg]
	if pack.is_installed:
		pass
	else:
		
