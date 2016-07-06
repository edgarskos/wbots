from core.log import *
import html
import sys
import re
from core.config import *

def fixblink(article ,text):
	if testmode == 1:
		printlog('testmode')
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
	printlog('fixblink testing site: '+ article)
	twobrackets = re.findall(r"\[(\S+)\]", text)
	for hit in twobrackets:
		link = str(hit)
		matches = re.search(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', link)
		if 'http://' not in link and 'https://' not in link and matches != None and 'ref' not in link and '@' not in link and '[' not in link:
			errorcout += 1
			linkpartlist = link.split('.')

			if len(linkpartlist) >= 3 and 'w' in linkpartlist[0]:
				if any((char in linkpartlist[0]) for char in characters):
					if any((char in linkpartlist[0]) for char in special):
						continue
				else:
					if len(linkpartlist[0]) != 3:
						log('invalid link: '+ link)
						linkpartlist[0] = 'www'
						time = 0
						finallink = ''
						for item in linkpartlist:
							time += 1
							if time != len(linkpartlist):
								finallink = finallink+item+'.'
							else:
								finallink = finallink+item
						link = '[http://'+finallink+']'
						log('should be: '+ link)
						fixedlinks.append(link)
						invalidlinks.append(link)

			else:
				log('invalid link: '+ link)
				link = '[http://'+link+']'
				log('should be: '+ link)
				fixedlinks.append(link)
				invalidlinks.append(link)

	printlog(str(errorcout)+' invalid links found')

	for fixedlink, invalidlink in zip(fixedlinks, invalidlinks):
		i = html.unescape(str(invalidlink))
		i = '['+i+']'
		f = html.unescape(str(fixedlink))
		text = text.replace(i, f)

	if text != oldtext:
		zeroedit = 1
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti korjasi linkkejä. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti korjasi linkin. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has fixed links. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has fixed link. "
	elif errorcout == 0:
		printlog('fixlinks no invalid links found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit