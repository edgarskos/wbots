from core.log import *
import re
from core.config import *

def textinen(article, text):
	errorcount = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0
	
	errorcount += text.count('[[Category:')+text.count('[[category:')

	text = text.replace('[[Category:', '[[Luokka:').replace('[[category:', '[[Luokka:')

	if text != oldtext:
		printlog('textinen error found: '+ article)
		if errorcount > 1 and lang == 'fi':
			saves = u"Botti muutti englanninkielisen luokka viitteen suomenkieliseksi. "
		elif errorcount == 1 and lang == 'fi':
			saves = u"Botti muutti englanninkieliset luokka viitteet suomenkielisiksi. "
		elif errorcount > 1 and lang == 'en':
			saves = u""
		elif errorcount == 1 and lang == 'en':
			saves = u""

	elif errorcount == 0:
		printlog('textinen error not found: '+ article)

	return errorcount, text, saves, zeroedit