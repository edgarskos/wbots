from bs4 import BeautifulSoup
from core.log import *
import html
import sys
import re
from core.config import *

def fixreflink(article ,text):
	errorcout = 0
	saves = ''
	zeroedit = 0
	linkpartlist = []
	fixedlinks = []
	invalidlinks = []
	text = str(text)
	oldtext = text
	characters = 'abcdefghijklmnopqrstuvxyzäöABCDEFGHIJKLMNOPQRSTUVXYZŽÄÖ!?*[]{}()0123456789'
	special = '!?*[]{}()'
	soup = BeautifulSoup(text, "lxml")


	for hit in soup.findAll('ref'):
		link = str(hit)
		orglink = link
		link = link.replace('<ref>', '').replace('</ref>', '')
		matches = re.search(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', link)
		if 'http://' not in link and 'https://' not in link and matches != None and 'ref' not in link and '@' not in link and '{' not in link[0:2]:
			errorcout += 1
			if '[' in link and ']' in  link:
				linkpartlist = link.split('.')
				if len(linkpartlist) >= 3 and 'w' in linkpartlist[0] and linkpartlist[0] != 'www':
					if '[' not in linkpartlist[0][0:1] and any((char in linkpartlist[0]) for char in characters):
						if any((char in linkpartlist[0]) for char in special):
							log('special mark found getting out')
							continue
					else:
						if len(linkpartlist[0]) != 3 or '[' in linkpartlist[0]:
							linkpartlist[0] = 'www'
							time = 0
							finallink = ''
							for item in linkpartlist:
								time += 1
								if time != len(linkpartlist):
									finallink = finallink+item+'.'
								else:
									finallink = finallink+item
							link = '<ref>[http://'+finallink+'</ref>'
							log('fixreflink invalid link found: '+article+'\n'+orglink+' --> '+link)
							fixedlinks.append(link)
							invalidlinks.append(orglink)
						else:
							printlog('www fix error: '+ str(linkpartlist))

				else:
					link = link.replace('[','')
					link = '<ref>[http://'+link+'</ref>'
					log('fixreflink invalid link found: '+article+'\n'+orglink+' --> '+link)
					fixedlinks.append(link)
					invalidlinks.append(orglink)
			else:
				linkpartlist = link.split('.')

				if len(linkpartlist) >= 3 and 'w' in linkpartlist[0] and linkpartlist[0] != 'www':
					if any((char in linkpartlist[0]) for char in characters):
						if any((char in linkpartlist[0]) for char in special):
							continue
					else:
						print(linkpartlist[0])
						if len(linkpartlist[0]) != 3:
							linkpartlist[0] = 'www'
							time = 0
							finallink = ''
							for item in linkpartlist:
								time += 1
								if time != len(linkpartlist):
									finallink = finallink+item+'.'
								else:
									finallink = finallink+item
							link = '<ref>http://'+finallink+'</ref>'
							log('fixreflink invalid link found: '+article+'\n'+orglink+' --> '+link)
							fixedlinks.append(link)
							invalidlinks.append(orglink)

						else:
							printlog('www fix error: '+ str(linkpartlist))

				else:
					link = '<ref>http://'+link+'</ref>'
					log('fixreflink invalid link found: '+article+'\n'+orglink+' --> '+link)
					fixedlinks.append(link)
					invalidlinks.append(orglink)

	for fixedlink, invalidlink in zip(fixedlinks, invalidlinks):
		i =  html.unescape(str(invalidlink))
		f = html.unescape(str(fixedlink))
		text = text.replace(i, f)

	if text != oldtext:
		zeroedit = 1
		printlog(str(errorcout)+' invalid links found')
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti korjasi linkkejä. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti korjasi linkin. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has fixed links. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has fixed link. "
	elif errorcout == 0:
		printlog('fixlinks invalid links not found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit