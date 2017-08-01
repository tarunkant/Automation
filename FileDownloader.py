
import urllib2
import re
from BeautifulSoup import BeautifulSoup
import os
import sys

url=sys.argv[1]

html_page = urllib2.urlopen(url)
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
	if(".java" in link.get('href')):
    		os.system("wget " +  url + link.get('href'))
    		