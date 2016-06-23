from bs4 import BeautifulSoup
from core.log import *
import html
import sys
import re
from core.config import *

def fixlink(article ,text):
	if testmode == 1:
		printlog('testmode')
	errorcout = 0
	saves = ''
	zeroedit = 0
	fixedlinks = []
	invalidlinks = []
	text = str(text)
	oldtext = text
	printlog('fixlink testing site: '+ article)
	soup = BeautifulSoup(text, "lxml")


	for hit in soup.findAll('ref'):
		link = str(hit)
		link = link.replace('<ref>', '').replace('</ref>', '')
		matches = re.search(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', link)
		if 'http://' not in link and 'https://' not in link and matches != None:
			errorcout += 1
			invalidlinks.append(link)
			if '[' in link and ']' in  link:
				printlog('invalid link: '+ link)
				link = link.replace('[','')
				link = '[http://'+link
				log('should be: '+ link)
				fixedlinks.append(link)
			else:
				log('invalid link: '+ link)
				link = 'http://'+link
				log('should be: '+ link)
				fixedlinks.append(link)

	printlog(str(errorcout)+' invalid links found')

	for fixedlink, invalidlink in zip(fixedlinks, invalidlinks):
		log(fixedlink, invalidlink)
		i =  html.unescape(str(invalidlink))
		f = html.unescape(str(fixedlink))
		text = text.replace(i, f)

	if text != oldtext:
		zeroedit = 1
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti korjasi linkkejä. "
		elif errorcout == 1 and lang == 'fi':
			save = u"Botti korjasi linkin. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has fixed links. "
		elif errorcout == 1 and lang == 'en':
			save = u"Bot has fixed link. "

	return errorcout, text, saves, zeroedit