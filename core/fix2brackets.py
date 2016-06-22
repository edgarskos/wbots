import pywikibot
from core.log import *
from pywikibot import pagegenerators
import re
from core.config import *

def fix2brackets(article):
	if testmode == 1:
		printlog('testmode')
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
				print('invalid link found')
				log('found link with two brackets: '+ item)
				olditem = '['+str(item)+']'
				log(olditem+' replaced with '+item)
				text = text.replace(olditem, str(item))

	if text != oldtext and testmode == 0:
		page.text = text
		if errorcout > 1:
			page.save(u"Botti korjasi linkkejä.")
		else:
			page.save(u"Botti korjasi linkin.")
	elif errorcout == 0:
		printlog('no invalid links found: '+ article)

	print()
	printlog('done')

	if text != oldtext and testmode == 1:
		log(text)
	return errorcout