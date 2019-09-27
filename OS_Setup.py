#!/usr/bin/env python3

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
line = "\n====================================================================\n"
var = platform.dist()
REPO = var[0]
USER = "mobius" ### place your user name here
PASSWD = "1"         ### palce your passwd here
REPONAME = var[0]
#KODENAME = var[1]
ARCH = platform.machine()
VERSION = var[1]
#INSTALL_MNGR =
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

dev_packages=[ "python-scapy","python-pip","python-networkx","python-netaddr","python-netifaces","python-netfilter","apt-transport-https","ca-certificates","curl","gnupg2","software-properties-common", "python-gnuplot", "python-mako", "python-radix", "ipython", "ipython3", "python-pycurl", "python-lxml", "python-nmap", "python-flask", "python-scrapy", "perl-modules", "build-essential", "cmake", "bison", "flex", "git"  ]
firmware_packages=[ "firmware-misc-nonfree",  "firmware-atheros", "firmware-brcm80211", "firmware-samsung", "firmware-realtek", "firmware-linux", "firmware-linux-free", "firmware-linux-nonfree", "intel-microcode", "firmware-zd1211" ]
gui_packages=[ "lightdm", "mate-desktop", "mate-desktop-environment",  "mate-desktop-environment-extra", "mate-desktop-environment-extras", "culmus", "mixxx", "guake", "bash-completion", "plank", "atom", "sqlitebrowser", "pgadmin3", "vim-gtk", "codeblocks", "ninja-ide", "geany", "geany-plugins", "wireshark", "zenmap", "transmission", "gparted", "vlc", "abiword", "owncloud-client", "vim", "plank", "moka-icon-theme", "faba-icon-theme" ]
lib_packages=[ "libpoe-component-pcap-perl", "libnet-pcap-perllibgtk2.0-dev", "libltdl3-dev", "libncurses-dev", "libusb-1.0-0-dev", "libncurses5-dev", "libbamf3-dev", "libdbusmenu-gtk3-dev", "libgdk-pixbuf2.0-dev", "libgee-dev", "libglib2.0-dev", "libgtk-3-dev", "libwnck-3-dev", "libx11-dev", "libgee-0.8-dev", "libnet1-dev", "libpcre3-dev", "libssl-dev", "libcurl4-openssl-dev", "libxmu-dev", "libpcap-dev", "libglib2.0", "libxml2-dev", "libpcap-dev", "libtool", "libsqlite3-dev", "libhiredis-dev", "libgeoip-dev", "libesd0-dev", "libncurses5-dev", "libusb-1.0-0", "libusb-1.0-0-dev", "libstdc++6-4.9-dbg"]


pack_to_install = []
###Func/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

#def bash(var):
#	os.system(var)


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
#def edit_files():
	#TODO:
	#		edit files : bash.bashrc, virc, vimrc, sysctl
	 

def pac_check(pkg):
	cache = apt.cache.Cache()
	#cache.update()

	
	pkg = cache[pkg]
	if pkg.is_installed:
		print "{pkg} already installed"
		pass
	else:
		pkg.mark_install()
		try:
			cache.commit()
		except Exception, arg :
			print "error with %s" %pkg

def exec_install():
	for i in packages:
		pac_check(i)

def main():
	if  os.getuid() != 0:
		print line
		print "\t\tGet R00T"
		print line
		exec_install;
		#edit_files;

###
#Main - _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _- _
###
if __name__ == "__main__":
	main()
