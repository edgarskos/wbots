from core.log import *
import re
from core.config import *
import html

def uc2um(article, text):
	errorcount = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0
	
	text = html.unescape(text)

	if text != oldtext:
		errorcount += 1

	

	if text != oldtext:
		zeroedit = 1
		printlog('uc2um error found: '+ article)
		if errorcount == 1 and lang == 'fi':
			saves = u"Botti muunsi [[unicode|unicode-syntaksin]] unicode merkeiksi. "
		elif errorcount == 1 and lang == 'en':
			saves = u"Bot has decoded unicode. "

	elif errorcount == 0:
		printlog('uc2um error found: '+ article)

	return errorcount, text, saves, zeroedit