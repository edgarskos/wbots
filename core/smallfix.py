from core.log import *
import re
from core.config import *

def smallfix(article, text):
	errorcout = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0
	
	errorlist = re.findall(r"\<.*?\>", text)

	for item in errorlist:
		if 'small' in item and len(item) <= 10:
			if '/' in item and item != '</small>':
				text = text.replace(item, '</small>')
				errorcout += 1
			elif '/' not in item and item != '<small>':
				text = text.replace(item, '<small>')
				errorcout += 1

	
	if text != oldtext:
		zeroedit = 1
		printlog('smallfix error found: '+ article)
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti korjasi small tagien syntaksit. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti korjasi small tagin syntaksin. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has fixed small tags syntaxes. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has fixed small tag syntax. "

	elif errorcout == 0:
		printlog('smallfix error found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit