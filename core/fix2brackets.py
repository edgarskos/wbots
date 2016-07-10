from core.log import *
import re
from core.config import *

def fix2brackets(article, text):
	if testmode == 1:
		printlog('testmode')
	errorcout = 0
	text = str(text)
	oldtext = text
	saves = ''
	zeroedit = 0
	printlog('fix2brackets testing site: '+ article)
	twobrackets = re.findall(r"\[(.*?)\]", text)
	for item in twobrackets:
		location = text.index(item)
		if '[' in item:
			if 'https://' in item or 'http://' in item:
				if '|' not in text[location-3:location]:
					errorcout += 1
					print('invalid link found')
					location = text.index(item)+len(item)
					if ']' in text[location+1:location+2]:

						olditem = '['+str(item)+']]'
						item = item.replace('[', '')
						item = '['+item+']'
						log(olditem+' replaced with '+item)
						text = text.replace(olditem, str(item))
					else:
						olditem = '['+str(item)+']'
						item = item.replace('[', '')
						item = '['+item+']'
						log(olditem+' replaced with '+item)
						text = text.replace(olditem, str(item))
				else:
					printlog('found problem: '+ article)
					printlog(item)

	if text != oldtext:
		zeroedit = 1
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti poisti ylimääräiset hakasulkeet ulkoisista linkeistä. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti poisti ylimääräiset hakasulkeet ulkoisesta linkistä. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has removed excessive brackets from external links. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has removed excessive brackets from external link. "

	elif errorcout == 0:
		printlog('fix2brackets no invalid links found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit