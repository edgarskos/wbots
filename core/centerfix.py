from core.log import *
import re
from core.config import *

def centerfix(article, text):
	errorcout = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0

	errorlist = re.findall(r"\<.*?\>", text)

	for item in errorlist:
		if 'center' in item and len(item) <= 11:
			if '/' in item and item != '</center>':
				text = text.replace(item, '</center>')
				errorcout += 1
			elif '/' not in item and item != '<center>':
				text = text.replace(item, '<center>')
				errorcout += 1

	
	if text != oldtext:
		zeroedit = 1
		printlog('centerfix error found: '+ article)
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti korjasi center tagien syntaksit. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti korjasi center tagin syntaksin. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has fixed center tags syntaxes. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has fixed center tag syntax. "

	elif errorcout == 0:
		printlog('centerfix error not found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit