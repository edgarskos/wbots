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

	printlog('done')

	return errorcout, text, saves, zeroedit