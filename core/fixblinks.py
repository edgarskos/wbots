from core.log import *
import html
import sys
import re
from core.config import *

def fixblink(article ,text):
	errorcount = 0
	saves = ''
	zeroedit = 0
	linkpartlist = []
	fixedlinks = []
	invalidlinks = []
	text = str(text)
	oldtext = text
	characters = 'abcdefghijklmnopqrstuvxyzäöABCDEFGHIJKLMNOPQRSTUVXYZŽÄÖ!?*[]{}()0123456789'
	special = '!?*[]{}()'
	twobrackets = re.findall(r"\[(\S+)\]", text)
	for hit in twobrackets:
		link = str(hit)
		matches = re.search(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', link)
		if 'http://' not in link and 'https://' not in link and matches != None and 'ref' not in link and '@' not in link and '[' not in link and '{' not in link[0:2]:
			orglink = '['+link+']'
			errorcount += 1
			linkpartlist = link.split('.')

			if len(linkpartlist) >= 3 and 'w' in linkpartlist[0] and linkpartlist[0] != 'www':
				if any((char in linkpartlist[0]) for char in characters):
					if any((char in linkpartlist[0]) for char in special):
						continue
				else:
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
						link = '[http://'+finallink+']'
						log('fixblink invalid link found: '+article+'\n'+orglink+' --> '+link)
						text = text.replace(orglink, link)
						fixedlinks.append(link)
						invalidlinks.append(orglink)
					else:
						printlog('www fix error')

			else:
				link = '[http://'+link+']'
				log('fixblink invalid link found: '+article+'\n'+orglink+' --> '+link)
				fixedlinks.append(link)
				invalidlinks.append(orglink)
				text = text.replace(orglink, link)

	

	if text != oldtext:
		zeroedit = 1
		printlog('fixblinks error found: '+ article)
		printlog(str(errorcount)+' invalid links found')
		if errorcount > 1 and lang == 'fi':
			saves = u"Botti korjasi linkkejä. "
		elif errorcount == 1 and lang == 'fi':
			saves = u"Botti korjasi linkin. "
		elif errorcount > 1 and lang == 'en':
			saves = u"Bot has fixed links. "
		elif errorcount == 1 and lang == 'en':
			saves = u"Bot has fixed link. "
	elif errorcount == 0:
		printlog('fixblinks error not found: '+ article)

	return errorcount, text, saves, zeroedit