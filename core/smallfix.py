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
	errorcout = text.count('<small/>')+text.count('< small/>')+text.count('<small />')+text.count('< small />')+text.count('</ small >')+text.count('</small >')+text.count('</ small>')

	text = text.replace('<small/>', '</small>').replace('< small />', '</small>').replace('< small/>', '</small>').replace('<small />', '</small>')
	text = text.replace('</ small >', '</small>').replace('</ small>', '</small>').replace('</small >', '</small>')
	
	if text != oldtext:
		zeroedit = 1
		printlog('smallfix invalid tags found: '+ article)
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti korjasi small tagien syntaksit. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti korjasi small tagin syntaksin. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has fixed small tags syntaxes. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has fixed small tag syntax. "

	elif errorcout == 0:
		printlog('smallfix invalid tags not found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit