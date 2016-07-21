#! /usr/bin/env python3
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
import re

url = 'https://fi.wikipedia.org/w/index.php?title=Toiminnot:Uudet_sivut&offset=&limit=500'


print('reading page')
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, "lxml")

tags = soup.findAll("a", {'class' : 'mw-newpages-pagename'})

for tag in tags:
	#print(tag)
	title = re.findall(r'title="(.*?)"', str(tag))
	file = open('articles', 'a')
	try:
		print(title[0])
		file.write(str(title[0]+'\n'))
	except:
		pass
