import sys
import re
from core.config import *
import pywikibot
from core.log import *


def fixpiped(article):
	if testmode == 1:
		printlog('testmode')
	fixeditem = None
	errorcout = 0
	site = pywikibot.Site()
	page = pywikibot.Page(site, article)
	text = str(page.text)
	oldtext = text
	printlog('fixpiped testing site: '+ article)
	searchtext = text.replace(' ', '_')
	twobrackets = re.findall(r"\[(\S+?)\]", searchtext )

	for item in twobrackets:
		fixeditem = None
		originalitem = item
		if '|' in item:
			print(item+' found')
			item = item.replace('[', '').replace(']', '')
			item = item.split('|')

			if item[0] == item[1]:
				fixeditem = '['+str(item[0])+''
				fixeditem = fixeditem.replace('_', ' ')
			if fixeditem != None:
				errorcout += 1
				originalitem = originalitem.replace('_', ' ')
				print(fixeditem)
				printlog(originalitem+'] --> '+fixeditem+']')
				text = text.replace(str(originalitem), str(fixeditem))

	return errorcout
