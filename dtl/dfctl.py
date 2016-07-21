#! /usr/bin/env python3
import sys

#path append
sys.path.append('../core/libs/')

import pywikibot
from pywikibot import pagegenerators

category = 'Pages_using_invalid_self-closed_HTML_tags'
print('reading page')
site = pywikibot.Site()
cat = pywikibot.Category(site,'Luokka:Pages using invalid self-closed HTML tags')
gen = pagegenerators.CategorizedPageGenerator(cat)

for page in gen:
	pagestr = str(page)
	pagestr = pagestr.replace(pagestr[0:5], '').replace(pagestr[len(pagestr)-2:len(pagestr)], '')
	print(pagestr)

	file = open('articles', 'a')
	try:
		file.write(str(pagestr+'\n'))
	except:
		pass