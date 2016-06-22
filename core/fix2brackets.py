import pywikibot
from core.log import *
from pywikibot import pagegenerators
import re

def fix2brackets(article):
	errorcout = 0
	site = pywikibot.Site()
	page = pywikibot.Page(site, article)
	text = str(page.text)
	oldtext = text
	printlog('fix2brackets testing site: '+ article)
	twobrackets = re.findall(r"\[(\S+)\]", text)
	for item in twobrackets:
		if '[' in item:
			if 'https://' in item or 'http://' in item:
				errorcout += 1
				log('found link with two brackets: '+ item)
				olditem = '['+str(item)+']'
				log(olditem+' replaced with '+item)
				text = text.replace(olditem, str(item))

		print(item)

	print(text)