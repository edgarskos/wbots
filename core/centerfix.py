from core.log import *
import re
from core.config import *

def centerfix(article, text):
	errorcount = 0
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
				errorcount += 1
			elif '/' not in item and item != '<center>':
				text = text.replace(item, '<center>')
				errorcount += 1

	
	if text != oldtext:
		zeroedit = 1
		printlog('centerfix error found: '+ article)
		if errorcount > 1 and lang == 'fi':
			saves = u"Botti korjasi center tagien syntaksit. "
		elif errorcount == 1 and lang == 'fi':
			saves = u"Botti korjasi center tagin syntaksin. "
		elif errorcount > 1 and lang == 'en':
			saves = u"Bot has fixed center tags syntaxes. "
		elif errorcount == 1 and lang == 'en':
			saves = u"Bot has fixed center tag syntax. "

	elif errorcount == 0:
		printlog('centerfix error not found: '+ article)

	return errorcount, text, saves, zeroedit