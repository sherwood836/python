# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import re

url = raw_input('Enter URL: ')
raw_count = raw_input('Enter count: ')
raw_pos = raw_input('Enter position: ')

for count in range(int(raw_count)) :
   html = urllib.urlopen(url).read()
   soup = BeautifulSoup(html)
   url = soup('a')[int(raw_pos) - 1].get('href', None)	

print re.findall("known_by_(\S+).html", url)[0]

