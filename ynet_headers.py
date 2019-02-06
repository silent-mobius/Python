#!/usr/bin/env python3

########################################################################
#
#
#
#
########################################################################

import lxml
import requests
from bs4 import BeautifulSoup


url='https://www.ynet.co.il/home/0,7340,L-8,00.html'

r = requests.get(url)

soup = BeautifulSoup(r.text, features='lxml')

for link in soup.select('a.smallheader'):
	print(link.text)
