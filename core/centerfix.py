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
	errorcout = text.count('<center/>')+text.count('< center/>')+text.count('<center />')+text.count('< center />')+text.count('</ center >')+text.count('</center >')+text.count('</ center>')

	text = text.replace('<center/>', '</center>').replace('< center />', '</center>').replace('< center/>', '</center>').replace('<center />', '</center>')
	text = text.replace('</ center >', '</center>').replace('</ center>', '</center>').replace('</center >', '</center>')
	
	if text != oldtext:
		zeroedit = 1
		printlog('centerfix invalid tags found: '+ article)
		if errorcout > 1 and lang == 'fi':
			saves = u"Botti korjasi center tagien syntaksit. "
		elif errorcout == 1 and lang == 'fi':
			saves = u"Botti korjasi center tagin syntaksin. "
		elif errorcout > 1 and lang == 'en':
			saves = u"Bot has fixed center tags syntaxes. "
		elif errorcout == 1 and lang == 'en':
			saves = u"Bot has fixed center tag syntax. "

	elif errorcout == 0:
		printlog('centerfix invalid tags not found: '+ article)
		oldtext = text

	return errorcout, text, saves, zeroedit