from core.log import *
import re
from core.config import *

def textinen(article, text):
	errorcout = 0
	text = str(text)
	oldtext = text
	checktext = text
	saves = ''
	zeroedit = 0
	
	errorcout += text.count('[[Category:')+text.count('[[category:')

	text = text.replace('[[Category:', '[[Luokka:').replace('[[category:', '[[Luokka:')

	if text != oldtext:
		printlog('textinen error found: '+ article)
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti muutti englanninkielisen luokka viitteen suomenkieliseksi. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti muutti englanninkieliset luokka viitteet suomenkielisiksi. "
		elif errorcout > 1 and lang == 'en':
			saves = u""
		elif errorcout == 1 and lang == 'en':
			saves = u""

	elif errorcout == 0:
		printlog('textinen error not found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit