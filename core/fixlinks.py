import pywikibot
from bs4 import BeautifulSoup
from core.log import *
from pywikibot import pagegenerators
import html
import sys
import re

def fixlink(article):
	test = 0
	errorcout = 0
	fixedlinks = []
	invalidlinks = []
	site = pywikibot.Site()
	page = pywikibot.Page(site, article)
	text = str(page.text)
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
				log('invalid link: '+ link)
				print('invalid link found')
				link = link.replace('[','')
				link = '[http://'+link
				log('should be: '+ link)
				fixedlinks.append(link)
			else:
				log('invalid link: '+ link)
				print('invalid link found')
				link = 'http://'+link
				log('should be: '+ link)
				fixedlinks.append(link)

		else:
			log('valid link: '+ link)

	printlog(str(errorcout)+' invalid links found')

	for fixedlink, invalidlink in zip(fixedlinks, invalidlinks):
		log(fixedlink, invalidlink)
		i =  html.unescape(str(invalidlink))
		f = html.unescape(str(fixedlink))
		text = text.replace(i, f)

	if text != oldtext and test != 1:
		page.text = text
		if errorcout > 1:
			page.save(u"Botti korjasi linkkejä.")
		else:
			page.save(u"Botti korjasi linkin.")
	elif errorcout == 0:
		printlog('no invalid links found: '+ article)