
import urllib2
import re
from BeautifulSoup import BeautifulSoup
import os
import sys

try:
	url=sys.argv[1]
except IndexError:
	print "Give url as command arguement"
try:
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page)
	for link in soup.findAll('a'):
		if(".java" in link.get('href')):
    			os.system("wget " +  url + link.get('href'))
    		
except NameError:
	print "Unable to read the file"
